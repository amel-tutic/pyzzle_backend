from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .algorithms import BreadthFirstSearch, BestFirstSearch, AStar
from .heuristics import HammingHeuristic, ManhattanHeuristic


@csrf_exempt
def run_bfs(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            size = data.get('size')
            initial_state = tuple(data.get('initial_state'))
            goal_state = tuple(data.get('goal_state'))

            bfs = BreadthFirstSearch(size)
            result = bfs.get_steps(initial_state, goal_state)

            return JsonResponse({'steps': result})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)


@csrf_exempt
def run_best_first_search(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            size = data.get('size')
            initial_state = tuple(data.get('initial_state'))
            goal_state = tuple(data.get('goal_state'))
            heuristic_type = data.get('heuristic')

            if heuristic_type == 'hamming':
                heuristic = HammingHeuristic()
            elif heuristic_type == 'manhattan':
                heuristic = ManhattanHeuristic()
            else:
                return JsonResponse({'error': 'Invalid heuristic'}, status=400)

            bfs = BestFirstSearch(size, heuristic)
            result = bfs.get_steps(initial_state, goal_state)

            return JsonResponse({'steps': result})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)


@csrf_exempt
def run_a_star(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            size = data.get('size')
            initial_state = tuple(data.get('initial_state'))
            goal_state = tuple(data.get('goal_state'))
            heuristic_type = data.get('heuristic')

            if heuristic_type == 'hamming':
                heuristic = HammingHeuristic()
            elif heuristic_type == 'manhattan':
                heuristic = ManhattanHeuristic()
            else:
                return JsonResponse({'error': 'Invalid heuristic'}, status=400)

            astar = AStar(size, heuristic)
            result = astar.get_steps(initial_state, goal_state)

            return JsonResponse({'steps': result})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

