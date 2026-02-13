# Copyright 2013-2023 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT
# file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import tempfile

from spack.package import *


class PyDmTree(PythonPackage):
    """tree is a library for working with nested data structures."""

    homepage = "https://github.com/deepmind/tree"
    pypi = "dm-tree/dm-tree-0.1.9.tar.gz"

    maintainers("aweits")

    version("0.1.9", sha256="a4c7db3d3935a5a2d5e4b383fc26c6b0cd6f78c6d4605d3e7b518800ecd5342b")
    version("0.1.8", sha256="0fcaabbb14e7980377439e7140bd05552739ca5e515ecb3119f234acee4b9430")
    version("0.1.7", sha256="30fec8aca5b92823c0e796a2f33b875b4dccd470b57e91e6c542405c5f77fd2a")
    version("0.1.6", sha256="6776404b23b4522c01012ffb314632aba092c9541577004ab153321e87da439a")
    version("0.1.5", sha256="a951d2239111dfcc468071bc8ff792c7b1e3192cab5a3c94d33a8b2bda3127fa")

    depends_on("py-setuptools", type="build")

    depends_on("python@3.6:", when="@:0.1.6", type=("build", "run"))
    depends_on("python@3.8:", when="@0.1.7:", type=("build", "run"))

    depends_on("cmake@3.18:", when="@0.1.7:", type="build")
    depends_on("bazel@:5", when="@:0.1.6", type="build")

    depends_on("py-six@1.12.0:", when="@:0.1.6", type=("build", "run"))
    depends_on("py-absl-py@0.6.1:", when="@0.1.7:", type=("build", "run"))
    depends_on("py-attrs@18.2.0:", when="@0.1.7:", type=("build", "run"))
    depends_on("py-wrapt@1.11.2:", when="@0.1.7:", type=("build", "run"))
    depends_on("py-numpy@1.21:", when="@0.1.7:", type=("build", "run"))
    depends_on("py-numpy@1.21.2:", when="@0.1.7: ^python@3.10:", type=("build", "run"))
    depends_on("py-numpy@1.23.3:", when="@0.1.7: ^python@3.11:", type=("build", "run"))
    depends_on("py-numpy@1.26.0:", when="@0.1.7: ^python@3.12:", type=("build", "run"))
    depends_on("py-numpy@2.1.0:", when="@0.1.7: ^python@3.13:", type=("build", "run"))

    # This is set for bazel-based builds only
    tmp_path = None

    def patch(self):
        if not self.spec.satisfies("@:0.1.6"):
            return

        PyDmTree.tmp_path = tempfile.mkdtemp(prefix="spack")
        env["TEST_TMPDIR"] = PyDmTree.tmp_path
        env["HOME"] = PyDmTree.tmp_path
        args = [
            "'--nohome_rc',\n",
            "'--nosystem_rc',\n",
            "'--output_user_root={0}',\n".format(PyDmTree.tmp_path),
            "'build',\n",
            "'--color=no',\n",
            "'--jobs={0}',\n".format(make_jobs),
            "'--verbose_failures',\n",
            "'--spawn_strategy=local',\n",
            "'--action_env', 'PYTHONPATH={0}',\n".format(env["PYTHONPATH"]),
        ]
        filter_file("'build',", " ".join(args), "setup.py", string=True)

    @run_after("install")
    def clean_tmp(self):
        if PyDmTree.tmp_path:
            remove_linked_tree(PyDmTree.tmp_path)
            PyDmTree.tmp_path = None

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            python("-c", "import tree; print(tree.__version__)")
