# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCmake(PythonPackage):
    """CMake is an open-source, cross-platform family of tools designed to
    build, test and package software
    """

    homepage = "https://cmake.org"
    git = "https://github.com/scikit-build/cmake-python-distributions.git"
    pypi = "cmake/cmake-3.22.2.tar.gz"

    version("3.27.7", sha256="9f4a7c7be2a25de5901f045618f41b833ea6c0f647115201d38e4fdf7e2815bc")
    version("3.22.2", sha256="b5bd5eeb488b13cf64ec963800f3d979eaeb90b4382861b86909df503379e219")
    version("3.21.4", sha256="30fa5ed8a5ad66dcd263adb87f3ce3dc2d0ec0ac3958f5becff577e4b62cd065")
    version("3.18.0", sha256="52b98c5ee70b5fa30a8623e96482227e065292f78794eb085fdf0fecb204b79b")

    depends_on("ninja", type="build")
    depends_on("py-scikit-build@0.12:", type="build")
    depends_on("py-setuptools@42:", type="build")
    # in newer pip versions --install-option does not exist
    depends_on("py-pip@:23.0", type="build")
    depends_on("git", type="build")
    depends_on("cmake@3.27.7", type=("build", "link", "run"), when="@3.27.7")
    depends_on("cmake@3.22.2", type=("build", "link", "run"), when="@3.22.2")
    depends_on("cmake@3.21.4", type=("build", "link", "run"), when="@3.21.4")
    depends_on("cmake@3.18.0", type=("build", "link", "run"), when="@3.18.0")
    depends_on("openssl")
    depends_on("pkgconfig")

    # see:
    #   https://github.com/scikit-build/cmake-python-distributions/issues/227
    #   https://github.com/spack/spack/pull/28760#issuecomment-1029362288
    for v in ["3.27.7", "3.22.2", "3.21.4", "3.18.0"]:
        resource(
            name="cmake-src",
            git="https://gitlab.kitware.com/cmake/cmake.git",
            commit="v{0}".format(v),
            when="@{0}".format(v),
            destination="cmake-src",
            placement="cmake-src",
        )

    def install_options(self, spec, prefix):
        return [
            "-DBUILD_CMAKE_FROM_SOURCE=ON",
            "-DCMakeProject_SOURCE_DIR=cmake-src",
        ]

    def setup_build_environment(self, env):
        env.append_flags(
            "SKBUILD_CONFIGURE_OPTIONS",
            "-DBUILD_TESTING=OFF -DRUN_CMAKE_TEST=OFF",
        )

    def patch(self):
        filter_file(
            'option(RUN_CMAKE_TEST "Run CMake test suite when built from sources" ON)',
            'option(RUN_CMAKE_TEST "Run CMake test suite when built from sources" OFF)',
            join_path(self.stage.source_path, "CMakeLists.txt"),
        )
