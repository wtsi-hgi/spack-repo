# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPbr(PythonPackage):
    """Python Build Reasonableness (pbr)."""

    homepage = "https://docs.openstack.org/pbr/latest/"
    pypi = "pbr/pbr-5.2.1-py2.py3-none-any.whl"

    # Use wheels to avoid legacy setup.py build paths that fail with newer
    # setuptools (bdist_wininst, deprecated options, etc.).
    version(
        "7.0.3",
        sha256="ff223894eb1cd271a98076b13d3badff3bb36c424074d26334cd25aebeecea6b",
        expand=False,
        url="https://files.pythonhosted.org/packages/c0/db/61efa0d08a99f897ef98256b03e563092d36cc38dc4ebe4a85020fe40b31/pbr-7.0.3-py2.py3-none-any.whl",
    )
    version(
        "5.2.1",
        sha256="0ce920b865091450bbcd452b35cf6d6eb8a6d9ce13ad2210d6e77557f85cf32b",
        expand=False,
        url="https://files.pythonhosted.org/packages/49/a2/e641de6c7e559e0a03a8d3c7b42199158b17a8cf2f96e11e7f725c2e730d/pbr-5.2.1-py2.py3-none-any.whl",
    )

    depends_on("python@2.7:", when="@:5", type=("build", "run"))
    depends_on("python@3.8:", when="@6:", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        # Basic import test
        with working_dir("spack-test", create=True):
            python("-c", "import pbr")
