# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyvis(PythonPackage):
    """Python library for visualizing networks."""

    homepage = "https://github.com/WestHealth/pyvis"
    url = "https://files.pythonhosted.org/packages/ab/4b/e37e4e5d5ee1179694917b445768bdbfb084f5a59ecd38089d3413d4c70f/pyvis-0.3.2-py3-none-any.whl"

    version("0.3.2", sha256="5720c4ca8161dc5d9ab352015723abb7a8bb8fb443edeb07f7a322db34a97555", expand=False)
