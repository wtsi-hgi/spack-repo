# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCmd2(PythonPackage):
    """Framework for building feature-rich interactive command line apps."""

    homepage = "https://cmd2.readthedocs.io/en/stable/"
    pypi = "cmd2/cmd2-3.0.0.tar.gz"

    license("MIT")

    version("3.0.0", sha256="f6fab21d2b344a3ab9fe174a6286c9fb4f43a185ad1dfacd13ef017a26a2c333")

    depends_on("py-setuptools", type="build")
    depends_on("py-wheel", type="build")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-pyperclip@1.8.2:", type=("build", "run"))
    depends_on("py-rich@14.1.0:", type=("build", "run"))
    depends_on("py-rich-argparse@1.7.1:", type=("build", "run"))
    depends_on("py-backports-strenum", when="^python@3.10:3.10", type=("build", "run"))

    @run_before("install")
    def fix_pyproject_metadata(self):
        # cmd2's pyproject.toml uses the legacy PEP 621 `license = "MIT"` form
        # which setuptools rejects (expects `license = {text=...}` or `{file=...}`).
        # Make it unambiguous and remove license-files (setuptools validates it separately).
        pyproject = join_path(self.stage.source_path, "pyproject.toml")
        filter_file(r'^[ \t]*license[ \t]*=[ \t]*"MIT"[ \t]*$', 'license = {text = "MIT"}', pyproject)
        filter_file(r"^license-files[ \t]*=[^\n]*\n", "", pyproject)
        filter_file(r"^license-files[ \t]*=[^\n]*$", "", pyproject)

        # Also strip future trove classifiers not yet recognized by older tooling.
        filter_file(r'^[ \t]*"Programming Language :: Python :: 3\.14",[ \t]*$', "", pyproject)
        filter_file(r'^[ \t]*"Programming Language :: Python :: 3\.15",[ \t]*$', "", pyproject)

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import cmd2")
