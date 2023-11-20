# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNdarrayListener(PythonPackage):
    """Implementation of the Observer pattern for NumPy arrays."""

    homepage = "https://github.com/limix/ndarray-listener"
    pypi = "ndarray_listener/ndarray_listener-2.0.1.tar.gz"

    version("2.0.1", sha256="2b740e733fa41612891f8b5eaec6d03794f696099b85c65e83d2669ae220455f")

    depends_on("py-numpy@1.13.0:", type=("build", "run"))
    depends_on("py-pytest@6.0.0:", type=("build", "run"))
