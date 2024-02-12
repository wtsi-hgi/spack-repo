# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMudata(PythonPackage):
    """In the same vein as AnnData is designed to represent unimodal annotated datasets in Python, MuData is designed to provide functionality to load, process, and store multimodal omics data."""

    homepage = "https://github.com/scverse/mudata"
    pypi = "mudata/mudata-0.2.3.tar.gz"

    version("0.2.3", sha256="45288ac150bfc598d68acb7c2c1c43c38c5c39522107e04f7efbf3360c7f2035")

    depends_on("py-flit-core", type="build")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-h5py", type=("build", "run"))
    depends_on("py-anndata@0.8:", type=("build", "run"))
