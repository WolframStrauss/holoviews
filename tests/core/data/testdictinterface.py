from collections import OrderedDict
import numpy as np

from holoviews.core.dimension import OrderedDict as cyODict
from holoviews.core.data import Dataset

from .base import HeterogeneousColumnTests, ScalarColumnTests, InterfaceTests


class DictDatasetTest(HeterogeneousColumnTests, ScalarColumnTests, InterfaceTests):
    """
    Test of the generic dictionary interface.
    """

    datatype = 'dictionary'
    data_type = (OrderedDict, cyODict)

    def test_dataset_simple_dict_sorted(self):
        dataset = Dataset({2: 2, 1: 1, 3: 3}, kdims=['x'], vdims=['y'])
        self.assertEqual(dataset, Dataset([(i, i) for i in range(1, 4)],
                                          kdims=['x'], vdims=['y']))

    def test_dataset_empty_list_init_dtypes(self):
        dataset = Dataset([], kdims=['x'], vdims=['y'])
        for d in 'xy':
            self.assertEqual(dataset.dimension_values(d).dtype, np.float64)

    def test_dataset_empty_combined_dimension(self):
        ds = Dataset({('x', 'y'): []}, kdims=['x', 'y'])
        ds2 = Dataset({'x': [], 'y': []}, kdims=['x', 'y'])
        self.assertEqual(ds, ds2)

    def test_dataset_ignore_non_dimensions(self):
        ds = Dataset({'x': [0, 1], 'y': [1, 2], 'ignore_scalar': 1,
                      'ignore_array': np.array([2, 3]), 'ignore_None': None},
                     kdims=['x', 'y'])
        ds2 = Dataset({'x': [0, 1], 'y': [1, 2]}, kdims=['x', 'y'])
        self.assertEqual(ds, ds2)
