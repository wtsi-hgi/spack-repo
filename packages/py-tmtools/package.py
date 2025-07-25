# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyTmtools(PythonPackage):
    """Python bindings around the TM-align code for structural alignment of proteins"""
    
    homepage = "https://github.com/jvkersch/tmtools"
    pypi = "tmtools/tmtools-0.2.0.tar.gz" 

    version("0.0.3", sha256="2477e29643d8cf1d1b6f0a1c9fe6ad40de6a2da2f0b50034c71557c628c02a7f")
    version("0.1.1", sha256="b900889d33b41bffecf76baef06b24600095211274df5f3ac376ab112745aa07")
    version("0.2.0", sha256="e2d6422f5af91ee41753fb2e9776140785eb818ec83d7aef8a8b2f296f05e72c")

    depends_on("py-setuptools", type=("build"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pybind11", type=("build", "run"))
