# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAttr(PythonPackage):
    """Simple decorator to set attributes of target function or class in a DRY way."""

    homepage = "https://github.com/denis-ryzhkov/attr"
    pypi = "attr/attr-0.3.2.tar.gz"

    version("0.3.2", sha256="1ceebca768181cdcce9827611b1d728e592be5d293911539ea3d0b0bfa1146f4")

    depends_on("py-setuptools", type="build")
