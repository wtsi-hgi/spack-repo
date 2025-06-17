# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGgplot(PythonPackage):
    """ggplot is a Python implementation of the grammar of graphics. It is not intended to be a feature-for-feature port of `ggplot2 for R <https://github.com/hadley/ggplot2>`__–though there is much greatness in ggplot2, the Python world could stand to benefit from it. So there will be feature overlap, but not neccessarily mimicry (after all, R is a little weird)."""

    homepage = "https://github.com/yhat/ggplot/"
    pypi = "ggplot/ggplot-0.11.5.tar.gz"

    version("0.11.5", sha256="48bbc9ea5987f815ad25856d76573506dbfe153ff696f026ce324582af56469f")

    depends_on("py-setuptools", type="build")
    depends_on("py-six", type=("build", "run"))
    depends_on("py-statsmodels", type=("build", "run"))
    depends_on("py-brewer2mpl", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-patsy@0.4:", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-cycler", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))

    def patch(self):
        filter_file("pd.tslib.Timestamp,", "pd.Timestamp,", "ggplot/utils.py", string=True)
        filter_file("pd.tslib.Timestamp,", "pd.Timestamp,", "ggplot/stats/smoothers.py", string=True)
        filter_file("from pandas.lib import Timestamp", "from pandas import Timestamp", "ggplot/stats/smoothers.py", string=True)
