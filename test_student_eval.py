import dtree_build
import sys
import csv
import discretize
import regression_tree

def main(col_names=None):
    # parse command-line arguments to read the name of the input csv file
    # and optional 'draw tree' parameter
    if len(sys.argv) < 2:  # input file name should be specified
        print ("Please specify input csv file name")
        retur01

    csv_file_name = sys.argv[1]

    data = []
    with open(csv_file_name) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            data.append(list(row))

    data = discretize.sort_variance(data)

    print("Total number of records = ",len(data))
    tree = regression_tree.buildtree(data, min_gain =0.006, min_samples = 5)

    regression_tree.printtree(tree, '', col_names)

    print("1: ", regression_tree.classify(['tenured', 'not minority', 'male', 'english', '60', '20', 'upper', '7', '4.3'], tree))
    print("2: ", regression_tree.classify(['tenured track', 'not minority', 'female', 'english', '50', '25', 'upper', '5', '4'], tree))
    print("3: ", regression_tree.classify(['teaching', 'not minority', 'male', 'english', '30', '15', 'upper', '8', '3.8'], tree))




    max_tree_depth = regression_tree.max_depth(tree)
    print("max number of questions=" + str(max_tree_depth))

    if len(sys.argv) > 2: # draw option specified
        import rtree_draw
        rtree_draw.drawtree(tree, jpeg=csv_file_name+'.jpg')

    if len(sys.argv) > 3:  # create json file for d3.js visualization
        import json
        import dtree_to_json
        json_tree = dtree_to_json.dtree_to_jsontree(tree, col_names)
        print(json_tree)

        # create json data for d3.js interactive visualization
        with open(csv_file_name + ".json", "w") as write_file:
            json.dump(json_tree, write_file)


if __name__ == "__main__":
    col_names = ['rank',
                 'ethnicity',
                 'gender',
                 'language',
                 'age',
                 'class_size',
                 'cls_level',
                 'bty_avg',
                 'prof_eval']
    main(col_names)
