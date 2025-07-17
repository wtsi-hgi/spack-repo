# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClustersignificance(RPackage):
    """The ClusterSignificance package provides tools to assess if class clusters in dimensionality reduced data representations have a separation different from permuted data

    The ClusterSignificance package provides tools to assess if class clusters in dimensionality reduced data representations have a separation different from permuted data. The term class clusters here refers to, clusters of points representing known classes in the data. This is particularly useful to determine if a subset of the variables, e.g. genes in a specific pathway, alone can separate samples into these established classes. ClusterSignificance accomplishes this by, projecting all points onto a one dimensional line. Cluster separations are then scored and the probability of the seen separation being due to chance is evaluated using a permutation method.
    """

    homepage = "https://github.com/jasonserviss/ClusterSignificance/"
    bioc = "ClusterSignificance"

    version("1.36.0", commit="38b3e5d54474ffb52a2d50e515f6f535ee678f4a")
    version("1.30.0", commit="8e6f5f18733afde352a8af19b648397438f1b281")

    depends_on("r@3.3:", type=("build", "run"))
    depends_on("r-pracma", type=("build", "run"))
    depends_on("r-princurve@2.0.5:", type=("build", "run"))
    depends_on("r-scatterplot3d", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
