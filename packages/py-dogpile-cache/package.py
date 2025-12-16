# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDogpileCache(PythonPackage):
    """Dogpile cache region abstraction layer."""

    homepage = "https://dogpilecache.sqlalchemy.org/"
    pypi = "dogpile.cache/dogpile_cache-1.5.0.tar.gz"

    license("MIT")

    version("1.5.0", sha256="849c5573c9a38f155cd4173103c702b637ede0361c12e864876877d0cd125eec")

    depends_on("python@3.10:", type=("build", "run"))

    depends_on("py-setuptools", type="build")
    depends_on("py-wheel", type="build")

    depends_on("py-decorator@4:", type=("build", "run"))
    depends_on("py-stevedore@3:", type=("build", "run"))
    depends_on("py-typing-extensions@4.0.1:", when="^python@:3.10", type=("build", "run"))

    @run_before("install")
    def fix_pyproject_toml(self):
        # With older setuptools (e.g. 68.x) dogpile.cache's pyproject.toml
        # triggers schema validation errors during metadata generation.
        pyproject = join_path(self.stage.source_path, "pyproject.toml")
        # Avoid `\s` here (it matches newlines) to keep substitutions single-line.
        filter_file(r'^license[ \t]*=[ \t]*"MIT"[ \t]*$', 'license = {file = "LICENSE"}', pyproject)
        # Remove the entire line (including its newline) to avoid creating invalid TOML.
        filter_file(r"^license-files[ \t]*=[^\n]*\n", "", pyproject)
        filter_file(r"^license-files[ \t]*=[^\n]*$", "", pyproject)

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import dogpile.cache")
