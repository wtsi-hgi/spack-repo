# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyScanpy(PythonPackage):
    """Scanpy is a scalable toolkit for analyzing single-cell
    gene expression data built jointly with anndata."""

    homepage = "https://scanpy.readthedocs.io/en/stable/"
    pypi = "scanpy/scanpy-1.9.1.tar.gz"

    license("BSD-3-Clause")

    version("1.9.8", sha256="2ab1790d2b82eadb0cf8d487f468beac7a8f6a3a8fd7112d1ae989f8c52a4353")
    version("1.9.7", sha256="c8cf5a4f1246e9dc5486d0ae9ac4950dc6fb5fa92c247cb571f96ff8e72145df")
    version("1.9.6", sha256="b2f24e6f220cb9d4d893b24f6899ba1a14cf2fef50b7e05bb37980c78de8a013")
    version("1.9.5", sha256="1d90f95cd5e103c9e0cc41fd84c1f2d81d86d6337cbe294316578ed071d39d82")
    version("1.9.4", sha256="14957604d251c665d42a8fe55b51b6d19867c3e987054b12e65c762d13664463")
    version("1.9.1", sha256="00c9a83b649da7e0171c91e9a08cff632102faa760614fd05cd4d1dbba4eb541")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools-scm", type="build")
    depends_on("py-flit-core@3.4:3", type="build")
    depends_on("py-importlib-metadata@0.7:", type=("build", "run"), when="^python@:3.7")
    depends_on("py-tomli", type="build")
    depends_on("py-packaging", type=("build", "run"))
    depends_on("py-anndata@0.7.4:0.9", type=("build", "run"))
    depends_on("py-numpy@1.17.0:", type=("build", "run"))
    depends_on("py-matplotlib@3.4:", type=("build", "run"))
    depends_on("py-pandas@1.0:", type=("build", "run"))
    depends_on("py-scipy@1.4:", type=("build", "run"))
    depends_on("py-seaborn", type=("build", "run"))
    depends_on("py-h5py@3:", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-scikit-learn@0.22:", type=("build", "run"))
    depends_on("py-statsmodels@0.10.0:", type=("build", "run"))
    depends_on("py-patsy", type=("build", "run"))
    depends_on("py-networkx@2.3:", type=("build", "run"))
    depends_on("py-natsort", type=("build", "run"))
    depends_on("py-joblib", type=("build", "run"))
    depends_on("py-numba@0.41.0:", type=("build", "run"))
    depends_on("py-umap-learn@0.3.10:", type=("build", "run"))
    depends_on("py-session-info", type=("build", "run"))
    depends_on("py-scikit-misc", type=("build", "run"))
