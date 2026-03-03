# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBioimageioCore(PythonPackage):
    """Python specific core utilities for running models in the BioImage Model Zoo."""

    homepage = "https://github.com/bioimage-io/core-bioimage-io-python"
    pypi = "bioimageio.core/bioimageio.core-0.5.11.tar.gz"

    version("0.5.11", sha256="d52947c5f8d77ebfcab7d0b91f60544acadbbf15fbbc7e8cfc0600c9db24da38")

    depends_on("py-bioimageio-spec@0.4.9:0.5", type=("build", "run"))
    depends_on("py-imageio@2.5:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-ruamel-yaml", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-xarray", type=("build", "run"))
    depends_on("py-tifffile", type=("build", "run"))
