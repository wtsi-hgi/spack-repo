# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyRdkit(PythonPackage):
    """A collection of chemoinformatics and machine-learning software written in C++ and Python"""
    
    homepage = "https://github.com/kuelumbus/rdkit-pypi"
    pypi = "rdkit/" 

    version("2025.3.3", sha256="a6a37db2e3b86e9e2e286a8b23a0f5954bf8ea5ea7a007e7a7be6e5f7eb95ac1", expand=False, url="https://files.pythonhosted.org/packages/0f/83/555cacdeba254d93bf6195984ee92a681f78f0c05d522e33a238d440ec04/rdkit-2025.3.3-cp310-cp310-manylinux_2_28_x86_64.whl")

    depends_on("py-setuptools", type=("build"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pillow", type=("build", "run"))
