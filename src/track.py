from deep_sort_realtime.deepsort_tracker import DeepSort

def get_tracker():
    return DeepSort(max_age=30, n_init=3, nms_max_overlap=1.0, embedder='mobilenet')
