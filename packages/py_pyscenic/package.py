# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyscenic(PythonPackage):
    """pySCENIC is a lightning-fast python implementation of the SCENIC pipeline (Single-Cell rEgulatory Network Inference and Clustering) which enables biologists to infer transcription factors, gene regulatory networks and cell types from single-cell RNA-seq data."""

    homepage = "http://scenic.aertslab.org/"
    pypi = "pyscenic/pyscenic-0.12.1.tar.gz"

    version("0.12.1", sha256="ae8fafa707d2578ffe08f9eed85f14a4cd9e1b53d57217420e2e956f0a8ddba2")

    depends_on("py-setuptools", type="build")

    depends_on("py-ctxcore@0.2.0:", type=("build", "run"))
    depends_on("py-cytoolz", type=("build", "run"))
    depends_on("py-multiprocessing-on-dill", type=("build", "run"))
    depends_on("py-llvmlite", type=("build", "run"))
    depends_on("py-numba@0.51.2:", type=("build", "run"))
    depends_on("py-attrs", type=("build", "run"))
    depends_on("py-frozendict", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas@1.3.5:", type=("build", "run"))
    depends_on("py-numexpr", type=("build", "run"))
    depends_on("py-cloudpickle", type=("build", "run"))
    depends_on("py-dask", type=("build", "run"))
    depends_on("py-distributed", type=("build", "run"))
    depends_on("py-arboreto@0.1.6:", type=("build", "run"))
    depends_on("py-boltons", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-interlap", type=("build", "run"))
    depends_on("py-umap-learn", type=("build", "run"))
    depends_on("py-loompy", type=("build", "run"))
    depends_on("py-networkx", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-fsspec", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-aiohttp", type=("build", "run"))
    depends_on("py-scikit-learn@0.22.2:", type=("build", "run"))
