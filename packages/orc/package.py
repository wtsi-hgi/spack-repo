# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Orc(CMakePackage):
    """The smallest, fastest columnar storage for Hadoop workloads."""

    homepage = "https://orc.apache.org/"
    url = "https://github.com/apache/orc/archive/refs/tags/v2.0.1.tar.gz"

    license("BSD-2-Clause")

    version("2.0.1", sha256="3a57c1e13ffc490651270e143a85050e26204faa38ff6c412c94a74098ef8d98")
    version("2.0.0", sha256="19bc533074867b3bbc3c8c1a1bf489ba738e8fd257fa65990159c68736dae4a8")
    version("1.9.3", sha256="3037fd324a17994f55146aae342531c4a343fdc1ac698c5c6f0f5b7a75ece501")
    version("1.9.2", sha256="cb933316cd40d611bcd1a2ccc6805455efcf88b8027ada6b3888666d4afee63a")
    version("1.9.1", sha256="7f8bbc862521ae99889205fb788e4906ecaaa6e503f075f6d3b78eeda8649322")
    version("1.9.0", sha256="951b09fdcded6518a05674a238824eaf81ad5e971e1adbb231bea7333215a75e")
    version("1.8.7", sha256="3f622918dac0f0b5531de3f28995cbab4067736390f9b6cfd8edc168b84797e8")
    version("1.8.6", sha256="83f0b0ef62a22a0f6dcbfb7c3a3bd3ebfd5d0deb07445fe7a498d6cd37eedda6")
    version("1.8.5", sha256="196d5d26e8a8490e397c5fe2bc01f3117c9fa44b6e53be4775b4261a8b10b1ad")
    version("1.7.10", sha256="9e8c69c038b144ea5927ea7251947e1a4cf1e745a003b61eb8a2cdf8d0dbaaa0")
    version("1.6.5", sha256="df5885db8fa2e4435db8d486c6c7fc4e2c565d6197eee27729cf9cbdf36353c0")

    depends_on("maven")
    depends_on("openssl")
    depends_on("openjdk@17:")
    depends_on("zlib-api")
    depends_on("zlib@1.2.11:", when="^[virtuals=zlib-api] zlib")
    depends_on("pcre")
    depends_on("protobuf@3.5.1:")
    depends_on("zstd@1.4.5:")
    depends_on("snappy@1.1.7:")
    depends_on("lz4@1.7.5:")

    # patch("thirdparty.patch")

    # def setup_build_environment(self, env):
    #     env.set("ZLIB_HOME", self.spec["zlib-api"].prefix)
    #     env.set("LZ4_HOME", self.spec["lz4"].prefix)
    #     env.set("PROTOBUF_HOME", self.spec["protobuf"].prefix)
    #     env.set("ZSTD_HOME", self.spec["zstd"].prefix)
    #     env.set("SNAPPY_HOME", self.spec["snappy"].prefix)
    #     env.set("GTEST_HOME", self.spec["googletest"].prefix)

    def cmake_args(self):
        args = []
        args.append("-DCMAKE_CXX_FLAGS=" + self.compiler.cxx_pic_flag)
        args.append("-DCMAKE_C_FLAGS=" + self.compiler.cc_pic_flag)
        args.append("-DINSTALL_VENDORED_LIBS:BOOL=OFF")
        args.append("-DBUILD_LIBHDFSPP:BOOL=OFF")
        args.append("-DBUILD_TOOLS:BOOL=OFF")
        args.append("-DBUILD_CPP_TESTS:BOOL=OFF")

        for x in ("snappy", "zstd", "lz4", "protobuf"):
            args.append("-D{0}_HOME={1}".format(x.upper(), self.spec[x].prefix))

        args.append(self.define("ZLIB_HOME", self.spec["zlib-api"].prefix))

        return args
