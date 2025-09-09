# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDataclasses(PythonPackage):
    """Dataclasses backport for Python 3.6.

    For Python 3.7+ ``dataclasses`` is part of the standard library. To allow
    environments that explicitly request ``py-dataclasses`` to concretize with
    newer Python, this package becomes a no-op install on Python 3.7+.
    """

    homepage = "https://github.com/ericvsmith/dataclasses"
    pypi = "dataclasses/dataclasses-0.7.tar.gz"

    version("0.8", sha256="8479067f342acf957dc82ec415d355ab5edb7e7646b90dc6e2fd1d96ad084c97")
    version("0.7", sha256="494a6dcae3b8bcf80848eea2ef64c0cc5cd307ffc263e17cdf42f3e5420808e6")

    depends_on("py-setuptools", type="build")

    # Allow with Python 3.6 (uses backport) and Python 3.7+ (stdlib module).
    # Only disallow Python <=3.5 where the backport doesn't support it.
    conflicts("^python@:3.5")

    def install(self, spec, prefix):
        # On Python >= 3.7, dataclasses is in the stdlib; perform a no-op install
        # so that explicit requests for this package don't conflict with newer Python.
        from spack.version import Version

        if spec["python"].version >= Version("3.7"):
            mkdirp(prefix)
            return

        # On Python 3.6, install the backport as usual
        super().install(spec, prefix)

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            python("-c", "import dataclasses; print(dataclasses.__name__)")
