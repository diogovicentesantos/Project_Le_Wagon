run_cluster_label:
	python -c 'from model.clusters import get_cluster; get_cluster("pasta tomato mozzarella")'

run_recipe:
	python -c 'from model.recipe import get_selected_recipe_link_list; get_selected_recipe_link_list(90, "I would like a simple and nice recipe for my familly tonight")'
