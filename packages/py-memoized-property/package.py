# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyMemoizedProperty(PythonPackage):
    """Descriptor that caches computed values on first access."""

    homepage = "https://github.com/openvax/memoized-property"
    pypi = "memoized-property/memoized-property-1.0.3.tar.gz"

    version("1.0.3", sha256="4be4d0209944b9b9b678dae9d7e312249fe2e6fb8bdc9bdaa1da4de324f0fcf5")

    depends_on("py-setuptools", type="build")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import memoized_property")
