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

    # FIXME: Only add the python/pip/wheel dependencies if you need specific versions
    # or need to change the dependency type. Generic python/pip/wheel dependencies are
    # added implicity by the PythonPackage base class.
    # depends_on("python@2.X:2.Y,3.Z:", type=("build", "run"))
    # depends_on("py-pip@X.Y:", type="build")
    # depends_on("py-wheel@X.Y:", type="build")

    # FIXME: Add a build backend, usually defined in pyproject.toml. If no such file
    # exists, use setuptools.
    # depends_on("py-setuptools", type="build")
    # depends_on("py-hatchling", type="build")
    # depends_on("py-flit-core", type="build")
    # depends_on("py-poetry-core", type="build")

    depends_on("py-bioimageio-spec@0.4.9:0.5", type=("build", "run"))
    depends_on("py-imageio@2.5:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-ruamel-yaml", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-xarray", type=("build", "run"))
    depends_on("py-tifffile", type=("build", "run"))
