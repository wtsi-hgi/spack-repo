# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPycistopic(PythonPackage):
    """pycisTopic is a Python module to simultaneously identify cell states and cis-regulatory topics from single cell epigenomics data."""

    homepage = "https://pycistopic.readthedocs.io/"

    git = "https://github.com/aertslab/pycisTopic.git"

    version("1.0.2", tag="v1.0.2")
    version("1.0.1", tag="v1.0.1")
    version("1.0.0", tag="v1.0.0")

    depends_on("py-adjusttext", type=("build", "run"))
    depends_on("py-annoy", type=("build", "run"))
    depends_on("py-bbknn", type=("build", "run"))
    depends_on("py-ctxcore", type=("build", "run"))
    depends_on("py-cython", type=("build", "run"))
    depends_on("py-ipython", type=("build", "run"))
    depends_on("py-ipykernel", type=("build", "run"))
    depends_on("py-gensim", type=("build", "run"))
    depends_on("py-harmonypy", type=("build", "run"))
    depends_on("py-ipympl", type=("build", "run"))
    depends_on("py-leidenalg", type=("build", "run"))
    depends_on("py-lda", type=("build", "run"))
    depends_on("py-loompy", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-networkx", type=("build", "run"))
    depends_on("py-numba", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pyopenssl", type=("build", "run"))
    depends_on("py-pandas@1.5:", type=("build", "run"))
    depends_on("py-polars@0.17.0:", type=("build", "run"))
    depends_on("py-pybedtools", type=("build", "run"))
    depends_on("py-pyfasta", type=("build", "run"))
    depends_on("py-pyranges@:0.0.128", type=("build", "run"))
    depends_on("py-pybiomart", type=("build", "run"))
    depends_on("py-pybigwig", type=("build", "run"))
    depends_on("py-python-levenshtein", type=("build", "run"))
    depends_on("py-igraph", type=("build", "run"))
    depends_on("py-ray", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-scanpy", type=("build", "run"))
    depends_on("py-scanorama", type=("build", "run"))
    depends_on("py-scrublet", type=("build", "run"))
    depends_on("py-seaborn", type=("build", "run"))
    depends_on("py-statsmodels", type=("build", "run"))
    depends_on("py-tables", type=("build", "run"))
    depends_on("py-tmtoolkit", type=("build", "run"))
    #depends_on("py-typing", type=("build", "run"))
    depends_on("py-umap-learn", type=("build", "run"))
    depends_on("py-xlrd", type=("build", "run"))
    depends_on("py-papermill", type=("build", "run"))
    depends_on("py-beautifulsoup4", type=("build", "run"))
    depends_on("py-macs3", type=("build", "run"))
    depends_on("py-lxml", type=("build", "run"))
    depends_on("py-tspex", type=("build", "run"))
    depends_on("py-polars", type=("build", "run"))
    depends_on("py-pyscenic", type=("build", "run"))
    depends_on("py-loomxpy", type=("build", "run"))
    depends_on("py-scatac-fragment-tools", type=("build", "run"))
    depends_on("py-sphinx-rtd-theme", type=("build", "run"))
    depends_on("py-nbsphinx", type=("build", "run"))
    depends_on("py-nbsphinx-link", type=("build", "run"))
    depends_on("py-numpydoc", type=("build", "run"))
    depends_on("py-pyrle", type=("build", "run"))
