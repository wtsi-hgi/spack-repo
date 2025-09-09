# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPbr(PythonPackage):
    """Python Build Reasonableness (pbr)."""

    homepage = "https://docs.openstack.org/pbr/latest/"
    pypi = "pbr/pbr-5.2.1-py2.py3-none-any.whl"

    # Use a wheel to avoid legacy setup.py build paths that fail with newer
    # setuptools (bdist_wininst, deprecated options, etc.).
    version(
        "5.2.1",
        sha256="0ce920b865091450bbcd452b35cf6d6eb8a6d9ce13ad2210d6e77557f85cf32b",
        expand=False,
        url="https://files.pythonhosted.org/packages/49/a2/e641de6c7e559e0a03a8d3c7b42199158b17a8cf2f96e11e7f725c2e730d/pbr-5.2.1-py2.py3-none-any.whl",
    )

    # Build requirements are provided by the python_pip build system
    # (py-pip, py-wheel, py-setuptools) and python itself.

    @run_after("install")
    def install_test(self):
        # Basic import test
        with working_dir("spack-test", create=True):
            python("-c", "import pbr")

