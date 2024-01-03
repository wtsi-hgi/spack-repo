# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class Rstudio(CMakePackage):
    """RStudio is an integrated development environment (IDE) for R."""

    homepage = "www.rstudio.com/products/rstudio/"
    url = "https://github.com/rstudio/rstudio/archive/refs/tags/v1.4.1717.tar.gz"

    version("2023.12.0", url="https://github.com/rstudio/rstudio/archive/refs/tags/v2023.12.0+369.tar.gz", sha256="6ee6acdd361b526fdc5fc922600cec0f04a7fe8304ae62e5a65d5fd4c55e824c")
    version("2022.12.0", url="https://github.com/rstudio/rstudio/archive/refs/tags/v2022.12.0+353.tar.gz", sha256="e4f3503e2ad4229301360f56fd5288e5c8e769c490073dae7fe40366237ecce0", preferred=True)
    version("1.4.1743", sha256="f046b2e91d4b27794d989e9bb2d7ad951b913ae86ed485364fc5b7fccba9c927")
    version("1.4.1717", sha256="3af234180fd7cef451aef40faac2c7b52860f14a322244c1c7aede029814d261")

    variant("notebook", default=False, description="Enable notebook support.")
    variant("server", default=False, description="Build the server.")

    variant("R361", default=False, description="Build With R v3.6.1")
    variant("R403", default=False, description="Build With R v4.0.3")
    variant("R410", default=False, description="Build With R v4.1.0")
    variant("R413", default=False, description="Build With R v4.1.3")
    variant("R423", default=True, description="Build With R v4.2.3")
    variant("R430", default=False, description="Build With R v4.3.0")
    variant("R431", default=False, description="Build With R v4.3.1")

    depends_on("r@3.0.1:", type=("build", "run"))
    depends_on("r+X@3.6.1", type=("build", "run"), when="+server +R361")
    depends_on("r+X@4.0.3", type=("build", "run"), when="+server +R403")
    depends_on("r+X@4.1.0", type=("build", "run"), when="+server +R410")
    depends_on("r+X@4.1.3", type=("build", "run"), when="+server +R413")
    depends_on("r+X@4.2.3", type=("build", "run"), when="+server +R423")
    depends_on("r+X@4.3.0", type=("build", "run"), when="+server +R430")
    depends_on("r+X@4.3.1", type=("build", "run"), when="+server +R431")
    depends_on("cmake@3.4.3:", type="build")
    depends_on("pkg-config", type=("build", "link"))
    depends_on("ant", type="build")
    depends_on("boost+pic@1.69:", when="~server")
    depends_on("boost+pic+atomic+chrono+date_time+filesystem+iostreams+program_options+random+regex+system+thread@1.69:", when="+server")
    depends_on("boost@1.83:", when="@2023.12.0:")
    depends_on("qt+webkit@5.12:", when="~server")
    depends_on("patchelf@0.9:")
    depends_on("yaml-cpp@:0.6.3")  # find_package fails with newest version
    depends_on("node-js")
    depends_on("yarn")
    depends_on("pandoc@2.11.4:")
    depends_on("icu4c")
    depends_on("soci~static+boost+postgresql+sqlite cxxstd=11")
    depends_on("java@8:")

    with when("+server"):
        depends_on("linux-pam")
        depends_on("libuuid")
        depends_on("tclap")
        depends_on("npm", type="build")
        depends_on("quarto-cli@1.1.251")

    with when("+notebook"):
        depends_on("r-base64enc")
        depends_on("r-digest")
        depends_on("r-evaluate")
        depends_on("r-glue")
        depends_on("r-highr")
        depends_on("r-htmltools")
        depends_on("r-jsonlite")
        depends_on("r-knitr")
        depends_on("r-magrittr")
        depends_on("r-markdown")
        depends_on("r-mime")
        depends_on("r-rmarkdown")
        depends_on("r-stringi")
        depends_on("r-stringr")
        depends_on("r-tinytex")
        depends_on("r-xfun")
        depends_on("r-yaml")

    # to use node-js provided by spack
    patch(
        "https://src.fedoraproject.org/rpms/rstudio/raw/5bda2e290c9e72305582f2011040938d3e356906/f/0004-use-system-node.patch",
        sha256="4a6aff2b586ddfceb7c59215e5f4a03f25b08fcc55687acaa6ae23c11d75d0e8",
        when="@:1.4.1743"
    )

    patch("0000-unbundle-dependencies-common.patch", sha256="5bfc248530f466fe590c4c57df5677bea81fa221e19f2808452c80bf0c1c6cb4", when="@2022.12.0")
    patch("0000-unbundle-dependencies-common-23.patch", sha256="5bfc248530f466fe590c4c57df5677bea81fa221e19f2808452c80bf0c1c6cb4", when="@2023.12.0")
    patch("0004-use-system-node.patch", sha256="464f8f99988a2fdb3c61917e60fcee8a07cbb73582e06650e3d7d17e9a2dd67f", when="@2022.12.0")
    patch("0004-use-system-node-23.patch", sha256="eaf7dedf6e4fb351e894aecde19375af243e7aa347f4b9747b610ed3634c8d8d", when="@2023.12.0")
    patch("0005-disable-quarto.patch", sha256="248b9ac70919f795a5ae4b639dd28b8936b597f19b0df3a356af8be860917f9b", when="@2023.12.0")

    patch("set.patch", when="@:2022.12.0")
    patch("const.patch", when="@:1.4.1743")
    patch("browserContext.patch", when="+server")

    def cmake_args(self):
        args = [
            "-DRSTUDIO_TARGET=Server" if "+server" in self.spec else "-DRSTUDIO_TARGET=Desktop",
            "DCMAKE_BUILD_TYPE=Release",
            "-DRSTUDIO_PACKAGE_BUILD=Yes",
            "-DRSTUDIO_USE_SYSTEM_YAML_CPP=Yes",
            "-DRSTUDIO_USE_SYSTEM_BOOST=Yes",
            "-DRSTUDIO_USE_SYSTEM_SOCI=Yes",
            "" if "+server" in self.spec else '-DQT_QMAKE_EXECUTABLE="{0}"'.format(self.spec["qt"].prefix.bin.qmake),
        ]

        return args

    def setup_build_environment(self, env):
        env.set("RSTUDIO_TOOLS_ROOT", self.prefix.tools)

        if self.spec.satisfies("+server"):
            if self.spec.satisfies("@2022.12.0"):
                env.set("RSTUDIO_VERSION_MAJOR", "2022")
                env.set("RSTUDIO_VERSION_MINOR", "12")
                env.set("RSTUDIO_VERSION_PATCH", "0")
                env.set("RSTUDIO_VERSION_SUFFIX", "+369")

            if self.spec.satisfies("@2022.12.0"):
                env.set("RSTUDIO_VERSION_MAJOR", "2023")
                env.set("RSTUDIO_VERSION_MINOR", "12")
                env.set("RSTUDIO_VERSION_PATCH", "0")
                env.set("RSTUDIO_VERSION_SUFFIX", "+353")

            env.set("RSTUDIO_RELEASE_NAME", "hgi")

        env.prepend_path("PATH", self.spec["node-js"].prefix.bin)
        env.prepend_path("PATH", self.stage.path + "/spack-src/node_modules/.bin")

    def patch(self):
        # fix hardcoded path for node-js in use_system_node patch
        filter_file(
            '<property name="node.bin" value="/usr/bin/node"/>',
            '<property name="node.bin" value="{0}"/>'.format(self.spec["node-js"].prefix.bin.node),
            "src/gwt/build.xml",
            string=True,
        )
        filter_file(
            '<property name="yarn.bin" value="/usr/bin/yarn"/>',
            '<property name="yarn.bin" value="{0}"/>'.format(self.spec["yarn"].prefix.bin.yarn),
            "src/gwt/build.xml",
            string=True,
        )

        filter_file(
            '"bin/quarto/bin/tools"',
            '"' + self.spec["quarto-cli"].prefix + '/package/dist/bin/tools"',
            "src/cpp/session/include/session/SessionConstants.hpp",
            string=True,
        )
        filter_file(
            '"bin/quarto"',
            '"' + self.spec["quarto-cli"].prefix + '/package/dist/"',
            "src/cpp/session/include/session/SessionConstants.hpp",
            string=True,
        )

        # remove hardcoded soci path to use spack soci
        if self.spec["soci"].version <= Version("4.0.0"):
            soci_lib = self.spec["soci"].prefix.lib64
        else:
            soci_lib = self.spec["soci"].prefix.lib
        filter_file(
            'set(SOCI_LIBRARY_DIR "/usr/lib")',
            'set(SOCI_LIBRARY_DIR "{0}")'.format(soci_lib),
            "src/cpp/CMakeLists.txt",
            string=True,
        )

        # unbundle icu libraries
        filter_file(
            "${QT_LIBRARY_DIR}/${ICU_LIBRARY}.so",
            join_path(self.spec["icu4c"].prefix.lib, "${ICU_LIBRARY}.so"),
            "src/cpp/desktop/CMakeLists.txt",
            string=True,
        )

    @run_before("cmake")
    def install_deps(self):
        deps = Executable("./dependencies/common/install-dictionaries")
        deps()
        deps = Executable("./dependencies/common/install-mathjax")
        deps()

        if self.spec.satisfies("+server"):
            deps = Executable("./dependencies/common/install-quarto")
            deps()

            npm = Executable(self.spec["npm"].prefix.bin.npm)
            npm("i", "typescript")
            npm("i", "yarn")

            if self.spec.satisfies("@2023.12.0"):
                deps = Executable("./dependencies/common/install-panmirror")
                deps()
                npm("i", "--prefix","src/gwt/lib/quarto/", "--force")



        # two methods for pandoc
        # 1) replace install-pandoc:
        #    - link pandoc into tools/pandoc/$PANDOC_VERSION
        #      (this is what install-pandoc would do)
        #    - cmake then installs pandoc files from there into bin
        # 2) remove install-pandoc and cmake install step + link directly into bin

        # method 1)
        filter_file(
            'set(PANDOC_VERSION "2.11.4" CACHE INTERNAL "Pandoc version")',
            'set(PANDOC_VERSION "{0}" CACHE INTERNAL "Pandoc version")'.format(
                self.spec["pandoc"].version
            ),
            "src/cpp/session/CMakeLists.txt",
            string=True,
        )

        pandoc_dir = join_path(self.prefix.tools, "pandoc", self.spec["pandoc"].version)
        os.makedirs(pandoc_dir)
        with working_dir(pandoc_dir):
            os.symlink(self.spec["pandoc"].prefix.bin.pandoc, "pandoc")
            os.symlink(
                os.path.join(self.spec["pandoc"].prefix.bin, "pandoc-citeproc"), "pandoc-citeproc"
            )

        def setup_run_environment(self, env):
            env.append_path("RSTUDIO_WHICH_R", join_path(self.spec["r"].prefix.bin, "R"))
