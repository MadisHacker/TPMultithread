#include <cpr/cpr.h>
#include <iostream>
#include <fstream>
#include <nlohmann/json.hpp>
#include <Eigen/Dense>
 
using Eigen::MatrixXf;

using json = nlohmann::json;
using Eigen::VectorXf;

using namespace std;

class Task {
  public:
    //Attributes
    int identifier;
    float time;
    int size;
    MatrixXf a;
    VectorXf b;
    VectorXf x;

    //Methods
    Task(int id, int size, MatrixXf& a,VectorXf& b){
    this->identifier = id;
    this->a = a;
    this->b = b;
    this->size = size;
    this->time = 0;
    this->x = 0*VectorXf::Random(size);
};

    void work(){
    auto start = std::chrono::high_resolution_clock::now();
    this->x = this->a.colPivHouseholderQr().solve(this->b);
    auto end = std::chrono::high_resolution_clock::now();
    this->time = std::chrono::duration<float>(end-start).count();
};

    static Task from_json(json j){

    int id = j["identifier"];
    int size = j["size"];

    MatrixXf a(size, size);
    auto mat = j["a"];
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            a(i, j) = mat[i][j];
        }
    }
    VectorXf b(size);

    for (int i = 0; i < size; i++) {
        b(i) = j["b"][i];
    }

    Task t = Task(id, size, a, b);

    return t;

};
    json to_json(){

    json j;
    j["identifier"] = this->identifier;
    j["size"] = this->size;
    j["x"] = this->x;
    j["time"] = this->time;
    j["b"] = this->b;

    j["a"] = json::array();  
    for (int i = 0; i < size; i++) {
        std::vector<float> row(a(i), a(i) + size);  
        j["a"].push_back(row); 
    }

    return j;

    };
};


int main(int argc, char** argv) {
    cpr::Response r = cpr::Get(cpr::Url{"http://localhost:8000"});
    r.status_code;                  // 200
    r.header["content-type"];       // application/json; charset=utf-8
    json jsonval = json::parse(r.text);

    Task t = Task::from_json(jsonval);
    std::cout << "Work in progress" << endl;
    t.work();

    json jres = t.to_json();

    std::cout << "work time is"<< t.time << std::endl;

    cpr::Response e = cpr::Post(
        cpr::Url{"http://localhost:8000"},
        cpr::Header{{"Content-Type", "application/json"}}, // En-tête HTTP
        cpr::Body{jres.dump()} // Corps de la requête
    );

    return 0;
}