# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyBokeh(PythonPackage):
    """Statistical and novel interactive HTML plots for Python"""

    homepage = "https://bokeh.org/"
    pypi = "bokeh/bokeh-0.12.2.tar.gz"

    license("BSD-3-Clause")

    version("3.3.1", sha256="2a7b3702d7e9f03ef4cd801b02b7380196c70cff2773859bcb84fa565218955c")
    version("2.4.3", sha256="ef33801161af379665ab7a34684f2209861e3aefd5c803a21fbbb99d94874b03")
    version("2.4.1", sha256="d0410717d743a0ac251e62480e2ea860a7341bdcd1dbe01499a904f233c90512")
    version("2.4.0", sha256="6fa00ed8baab5cca33f4175792c309fa2536eaae7e90abee884501ba8c90fddb")
    version("2.3.3", sha256="a5fdcc181835561447fcc5a371300973fce4114692d5853addec284d1cdeb677")
    version("1.3.4", sha256="e2d97bed5b199a10686486001fed5c854e4c04ebe28859923f27c52b93904754")
    version("0.12.2", sha256="0a840f6267b6d342e1bd720deee30b693989538c49644142521d247c0f2e6939")

    depends_on("py-setuptools", type=("build", "run"), when="@1.3.4:2.4.3")
    depends_on("py-setuptools@64:65", type=("build", "run"), when="@3:")
    depends_on("py-setuptools-git-versioning", type="build", when="@3:")
    depends_on("py-colorama", type="build", when="@3:")

    depends_on("python@2.6:", type=("build", "run"), when="@0.12.2")
    depends_on("python@2.7:", type=("build", "run"), when="@1.3.4:")
    depends_on("python@3.6:", type=("build", "run"), when="@2.3.3:")
    depends_on("python@3.7:", type=("build", "run"), when="@2.4.0:")
    depends_on("python@3.8:", type=("build", "run"), when="@3.0.0:")
    depends_on("python@3.9:", type=("build", "run"), when="@3.2.0:")

    depends_on("py-requests@1.2.3:", type=("build", "run"), when="@0.12.2")
    depends_on("py-six@1.5.2:", type=("build", "run"), when="@:1.3.4")
    depends_on("py-python-dateutil@2.1:", type=("build", "run"), when="@:2.3.3")

    depends_on("py-jinja2@2.7:", type=("build", "run"))
    depends_on("py-jinja2@2.9:", type=("build", "run"), when="@2.3.3:")

    depends_on("py-contourpy@1:", type=("build", "run"), when="@3:")

    depends_on("py-numpy@1.7.1:", type=("build", "run"))
    depends_on("py-numpy@1.11.3:", type=("build", "run"), when="@2.3.3:")
    depends_on("py-numpy@1.16:", type=("build", "run"), when="@3.1:")

    depends_on("py-packaging@16.8:", type=("build", "run"), when="@1.3.4:")

    depends_on("py-pandas@1.2:", type=("build", "run"), when="@3:")

    depends_on("pil@4.0:", type=("build", "run"), when="@1.3.4:")
    depends_on("pil@7.1.0:", type=("build", "run"), when="@2.3.3:")

    depends_on("py-pyyaml@3.10:", type=("build", "run"))

    depends_on("py-tornado@4.3:", type=("build", "run"))
    depends_on("py-tornado@5.1:", type=("build", "run"), when="@2.3.3:")

    depends_on("py-typing-extensions@3.7.4:", type=("build", "run"), when="@2.3.3:3.0.0")
    depends_on("py-typing-extensions@3.10.0:", type=("build", "run"), when="@2.4.0:3.0.0")

    depends_on("py-xyzservices@2021.09.1:", type=("build", "run"), when="@3:")
    # Use legacy pip API for <=2.4 to allow --install-option
    depends_on("py-pip@:23.0", type="build", when="@:2.4")

    def patch(self):
        # Older Bokeh (<=2.4.x) requires passing --build-js/--install-js explicitly
        # when building wheels/sdists. Pip/PEP517 builds in Spack don't pass these,
        # causing the build to error out. Inject a default of --install-js.
        if self.spec.satisfies("@:2.4"):
            filter_file(
                r"print\(f\"Error: Option '--build-js' or '--install-js' must be present with \{dist!r\}, exiting.\"\)\n\s*sys\.exit\(1\)",
                "print(f\"Info: defaulting to --install-js for {dist!r}.\")\n            sys.argv.append('--install-js')",
                "_setup_support.py",
            )

    def setup_build_environment(self, env):
        # Ensure the JS flag requirement does not abort wheel builds (pip/PEP517)
        if self.spec.satisfies("@:2.4"):
            import os
            support = join_path(self.stage.source_path, "_setup_support.py")
            if os.path.exists(support):
                # Neutralize hard exits by defaulting to --install-js
                filter_file(r"sys\.exit\(1\)", "sys.argv.append('--install-js')", support)

    @run_before("install")
    def preinstall_patch_js_flag(self):
        # As a backstop, patch just before install as well (ensures stage exists)
        if self.spec.satisfies("@:2.4"):
            import os
            support = join_path(self.stage.source_path, "_setup_support.py")
            if os.path.exists(support):
                filter_file(r"sys\.exit\(1\)", "pass", support)
                filter_file(r"sys\.argv\.append\('--install-js'\)", "pass", support)

    # Ensure PEP 517 builds pass the required JS flag for 2.4.x
    def config_settings(self, spec, prefix):
        if spec.satisfies("@:2.4"):
            # Forward setuptools build option to always install prebuilt JS
            # pip will pass this as: --config-settings=--build-option=--install-js
            return {"--build-option": "--install-js"}
        return {}

    def install_options(self, spec, prefix):
        if spec.satisfies("@:2.4"):
            # For pip<=23.0, ensure setup.py install receives the JS option
            return ["--install-js"]
        return []

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command.path
            self.run_test(python, options=["-c", "import bokeh; print(bokeh.__version__)"])
