# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Rdkit(CMakePackage):
    """RDKit is a collection of cheminformatics and machine-learning
    software written in C++ and Python."""

    homepage = "https://www.rdkit.org"
    url = "https://github.com/rdkit/rdkit/archive/refs/tags/Release_2021_03_2.tar.gz"

    maintainers("bvanessen", "RMeli")

    license("BSD-3-Clause")

    version("2024_03_3", sha256="52f79c6bf1d446cdb5c86a35de655d96bad0c52a5f4ecbe15f08eaf334e6f76a")

    # depends_on("c", type="build")  # generated
    # depends_on("cxx", type="build")  # generated
    # depends_on("fortran", type="build")  # generated

    variant("freetype", default=True, description="Build freetype support")

    with when("@2022_09_5:"):
        variant(
            "python",
            default=True,
            when="@2022_09_5:",
            description="Build standard Python wrappers",
        )
        variant("contrib", default=False, description="Build Contrib directory")
        variant("freesasa", default=False, description="Build freesasa wrapper")
        variant("coordgen", default=True, description="Build coordgen wrapper")
        variant("maeparser", default=True, description="Build MAE parser wrapper")
        variant("yaehmop", default=True, description="Build YAeHMOP wrapper")
        variant("xyz2mol", default=False, description="Build support for RDKit xyz2mol")
        variant("descriptors3d", default=True, description="Build 3D descriptors calculators")

        depends_on("freesasa", when="+freesasa")
        depends_on("coordgen", when="+coordgen")
        depends_on("maeparser", when="+maeparser")
        depends_on("eigen@3:", when="+descriptors3d")
        depends_on("python@3:", when="+python")
        depends_on("py-numpy", when="+python")
        # https://github.com/rdkit/rdkit/issues/7477
        depends_on("py-numpy@:1", when="@:2024.03.3+python")

        extends("python", when="+python")

        conflicts("+xyz2mol", when="~yaehmop", msg="XY2MOL requires YAeHMOP")

    depends_on("boost@1.53.0: +python +serialization +iostreams +system")
    depends_on("sqlite")
    depends_on("freetype", when="@2020_09_1: +freetype")


    def cmake_args(self):
        args = [
            "-DRDK_INSTALL_INTREE=OFF",
            self.define_from_variant("RDK_BUILD_FREETYPE_SUPPORT", "freetype"),
        ]
        if "@2022_09_5:" in self.spec:
            args.extend(
                [
                    self.define_from_variant("RDK_BUILD_PYTHON_WRAPPERS", "python"),
                    self.define_from_variant("RDK_BUILD_CONTRIB", "contrib"),
                    self.define_from_variant("RDK_BUILD_FREESASA_SUPPORT", "freesasa"),
                    self.define_from_variant("RDK_BUILD_COORDGEN_SUPPORT", "coordgen"),
                    self.define_from_variant("RDK_BUILD_MAEPARSER_SUPPORT", "maeparser"),
                    self.define_from_variant("RDK_BUILD_XYZ2MOL_SUPPORT", "xyz2mol"),
                    self.define_from_variant("RDK_BUILD_DESCRIPTORS3D", "descriptors3d"),
                ]
            )

        return args
