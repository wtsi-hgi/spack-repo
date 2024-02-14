# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyScenicplus(PythonPackage):
    """SCENIC+ is a python package to build gene regulatory networks (GRNs) using combined or separate single-cell gene expression (scRNA-seq) and single-cell chromatin accessibility (scATAC-seq) data."""

    homepage = "https://scenicplus.readthedocs.io/"
    url = "https://github.com/aertslab/scenicplus/archive/refs/tags/v1.0.0.tar.gz"

    version("1.0.0", sha256="99a1ea2be3708a10e49413fb8518e7a9bcb7363c761ee82384398742e084b7ac")

    depends_on("py-pandas@1.5:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-attr", type=("build", "run"))
    #depends_on("py-typing", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    #depends_on("py-statistics", type=("build", "run"))
    depends_on("py-pyranges", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-pybiomart", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-arboreto", type=("build", "run"))
    depends_on("py-gseapy@0.10.8:", type=("build", "run"))
    depends_on("py-networkx", type=("build", "run"))
    depends_on("py-ctxcore", type=("build", "run"))
    depends_on("py-seaborn", type=("build", "run"))
    depends_on("py-pybigwig", type=("build", "run"))
    depends_on("py-plotly", type=("build", "run"))
    depends_on("py-adjusttext", type=("build", "run"))
    depends_on("py-macs3", type=("build", "run"))
    depends_on("py-lxml", type=("build", "run"))
    depends_on("py-tspex", type=("build", "run"))
    depends_on("py-plotly", type=("build", "run"))
    depends_on("py-kaleido", type=("build", "run"))
    depends_on("py-pyvis", type=("build", "run"))
    depends_on("py-pygam", type=("build", "run"))
    depends_on("py-scanpy@1.9:", type=("build", "run"))
    depends_on("py-cython", type=("build", "run"))
    depends_on("py-plotnine", type=("build", "run"))
    depends_on("py-mudata", type=("build", "run"))
    depends_on("py-pycistopic", type=("build", "run"))
    depends_on("py-pycistarget", type=("build", "run"))
    depends_on("py-pyscenic", type=("build", "run"))
    depends_on("py-loomxpy", type=("build", "run"))
    depends_on("py-sphinx-rtd-theme", type=("build", "run"))
    depends_on("py-nbsphinx", type=("build", "run"))
    depends_on("py-nbsphinx-link", type=("build", "run"))
    depends_on("py-numpydoc", type=("build", "run"))
    depends_on("py-sphinx-book-theme", type=("build", "run"))
