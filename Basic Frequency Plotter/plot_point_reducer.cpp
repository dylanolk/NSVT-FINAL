//Nyquist-Shannon Converter
//Seth Spiegel
/*
    This program accepts a CSV file of plot points representing an audio frequency spectrogram 
    and returns a CSV file of reduced points according to the Nyquist-Shannon theorem that 
    should be completely lossless
*/

#include <vector>
#include <string>
#include <thread>
#include <fstream>
#include <iostream>

using namespace std;

vector<double> get_yvalues(const string &filename_)
{
    string line_;
    vector<double> values_;

    ifstream file_(filename_);

    if (file_.is_open())
    {
        while (getline(file_, line_))
        {
            float value = (float)atof(line_.c_str());
            values_.push_back(value);
        }
        
        file_.close();
        return values_;
    }
    else
    {
      cout << "Unable to open file" << endl;
    }
}


//takes in all the plot points and returns all the peaks and dips 
vector<vector<double>> highest_lowest (const vector<double> )
{
    
}

int main()
{
    vector<double> test = get_yvalues("y_values");
    //for (size_t i = 0; i < test.size(); i++)
    for (size_t i = 0; i < 200; i++)
    {
        cout << test[i] << " ";
    }
    

    return 0;
}