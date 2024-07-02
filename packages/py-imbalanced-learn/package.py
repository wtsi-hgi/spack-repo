# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyImbalancedLearn(PythonPackage):
    """imbalanced-learn is a python package offering a number of re-sampling
    techniques commonly used in datasets showing strong between-class imbalance.
    It is compatible with scikit-learn and is part of scikit-learn-contrib
    projects."""

    homepage = "https://github.com/scikit-learn-contrib/imbalanced-learn"
    pypi = "imbalanced-learn/imbalanced-learn-0.10.1.tar.gz"

    maintainers("meyersbs")

    license("MIT")

    version("0.12.3", sha256="5b00796a01419e9102bd425e27c319d58d1f6cf2dfa751e02ed7f4edf67c3c1b")
    version("0.12.2", sha256="a80c56cedcb07124f266be62d3a5d2ab5b5779909a7343fdf1b993479662f6c1")
    version("0.12.1", sha256="30cabc00d9209398bc28c17c3a1a7fd2af0cd21d24ae727e5882db2c3f8a3cbc")
    version("0.12.0", sha256="b9ccd9aaa3028699079d43a6d4d9fc9d039f55376733b31f87c7d9b125dcc165")
    version("0.11.0", sha256="7582ae8858e6db0b92fef97dd08660a18297ee128d78c2abdc006b8bd86b8fdc")
    version("0.10.1", sha256="bc7609619ec3c38c442292928239ad3d10b5deb0af8a29c83822b7b57b319f8b")

    # From setup.py:
    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-numpy@1.17.3:", type=("build", "run"))
    depends_on("py-scipy@1.3.2:", type=("build", "run"))
    depends_on("py-scikit-learn@1.0.2:", type=("build", "run"))

    variant("optional", default=False, description="Enable optional dependencies.")
    depends_on("py-pandas@1.0.5:", when="+optional", type=("build", "run"))
    depends_on("py-tensorflow@2.4.3:", when="+optional", type=("build", "run"))
    depends_on("py-keras@2.4.3:", when="+optional", type=("build", "run"))

    # From https://imbalanced-learn.org/stable/install.html#getting-started:
    depends_on("py-joblib@1.1.1:", type=("build", "run"))
    depends_on("py-threadpoolctl@2.0.0:", type=("build", "run"))
    depends_on("py-cython@0.29.24:", type="build")
