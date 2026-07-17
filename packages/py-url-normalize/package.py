# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyUrlNormalize(PythonPackage):
    """URL normalization for Python."""

    homepage = "https://github.com/niksite/url-normalize"
    pypi = "url-normalize/url-normalize-1.4.3.tar.gz"

    version("1.4.3", sha256="ec3c301f04e5bb676d333a7fa162fa977ad2ca04b7e652bfc9fac4e405728eed", expand=False, url="https://files.pythonhosted.org/packages/65/1c/6c6f408be78692fc850006a2b6dea37c2b8592892534e09996e401efc74b/url_normalize-1.4.3-py2.py3-none-any.whl")

    depends_on("python@3.6:3", type=("build", "run"))

    depends_on("py-six", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            python("-c", "import url_normalize")
