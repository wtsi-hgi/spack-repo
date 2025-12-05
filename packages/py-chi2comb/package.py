# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyChi2comb(PythonPackage):
    """Estimate CDFs of linear combinations of noncentral chi-squared RVs."""

    homepage = "https://github.com/limix/chi2comb-py"
    pypi = "chi2comb/chi2comb-0.1.0.tar.gz"

    version("0.1.0", sha256="e1605e065747a04c95a244ac4dd727af06a0f99a22f3d4ff549b2ebdcafee7aa")

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-cffi@1.11.5:", type=("build", "run"))
    depends_on("chi2comb", type=("build", "link", "run"))
    depends_on("py-pytest@5:", type="test")
    depends_on("py-pytest-doctestplus@0.8.0:", type="test")

    @run_after("install")
    def install_test(self):
        """Verify the module can be imported."""
        python = self.spec["python"].command
        with working_dir("spack-test", create=True):
            python("-c", "import chi2comb")
