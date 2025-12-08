# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyTypechecks(PythonPackage):
    """Helper functions for runtime type checking"""

    homepage = "https://github.com/openvax/typechecks"
    pypi = "typechecks/typechecks-0.1.0.tar.gz"

    version("0.0.0", sha256="65adc64b105c12f5b40085846103dfe301a4051b20c7b04047dd69a693e9d482")
    version("0.0.1", sha256="5d383f2373cd304ddda9b1d5eb091102b61ff00bbbb7090134be98076a39345a")
    version("0.0.2", sha256="1473dfecd9ceebb3608df3515cadd09bf87ca8385ae66839943bd373a6b9da36")
    version("0.1.0", sha256="7d801a6018f60d2a10aa3debc3af65f590c96c455de67159f39b9b183107c83b")

    depends_on("py-setuptools", type="build")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            python("-c", "import typechecks")
