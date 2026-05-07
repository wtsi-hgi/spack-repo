# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import re

from spack.package import *


class HsaRocrDev(CMakePackage):
    """This repository includes the user mode API nterfaces and libraries
    necessary for host applications to launch computer kernels to available
    HSA ROCm kernel agents.AMD Heterogeneous System Architecture HSA -
    Linux HSA Runtime for Boltzmann (ROCm) platforms."""

    homepage = "https://github.com/ROCm/ROCR-Runtime"
    git = "https://github.com/ROCm/rocm-systems.git"
    tags = ["rocm"]

    def url_for_version(self, version):
        if version <= Version("7.1.1"):
            url = "https://github.com/ROCm/ROCR-Runtime/archive/rocm-{0}.tar.gz"
        else:
            url = "https://github.com/ROCm/rocm-systems/archive/rocm-{0}.tar.gz"
        return url.format(version)

    maintainers("srekolam", "renjithravindrankannath", "haampie", "afzpatel")
    libraries = ["libhsa-runtime64"]

    version("master", branch="master")

    version("7.2.0", sha256="728ea7e9bf16e6ed217a0fd1a8c9afaba2dae2e7908fa4e27201e67c803c5638")
    version("7.1.1", sha256="4c5b58afa1e11461954bd005a10ebf29941c120f1d6a7863954597f5eacfc605")
    version("7.1.0", sha256="383fa8e1776c3ee527cdddc9f9ac6f7134c3fcd8758eae9be8bd3a8b7fdca9b1")
    version("7.0.2", sha256="9c2020f7a42d60fe9775865ab58464078007926a3b01f1ca8128557c89e7a566")
    version("7.0.0", sha256="9ea2cbcf343f643ede6e16d82fbd0303771e1978759b2e546d0efc0df3263e4c")
    version("6.4.3", sha256="3b23bed04cbed72304d31d69901eb76afa2099c7ac37f055348dfcda2d25e41a")
    version("6.4.2", sha256="8ad5dbf7cb0f728b8e515f46a41db24ed3b99ca894ccdd9f4d9bac969e9e35bb")
    version("6.4.1", sha256="f72d100a46a2dd9f4c870cef156604777f1bdb1841df039d14bf37b19814b9da")
    version("6.4.0", sha256="ff740e8c8f2229c6dc47577363f707b1a44ea4254f8ad74f8f0a669998829535")
    version("6.3.3", sha256="aa2e30d3d68707d6df4840e954bb08cc13cd312cec1a98a64d97adbe07262f50")
    version("6.3.2", sha256="aaecaa7206b6fa1d5d7b8f7c1f7c5057a944327ba4779448980d7e7c7122b074")
    version("6.3.1", sha256="547ceeeda9a41cdffa21e57809dc5834f94938a0a2809c283aebcbcf01901df0")
    version("6.3.0", sha256="8fd6bcd6a5afd0ae5a59e33b786a525f575183d38c34049c2dab6b9270a1ca3b")
    version("6.2.4", sha256="b7aa0055855398d1228c39a6f4feb7d7be921af4f43d82855faf0b531394bb9b")
    version("6.2.1", sha256="dbe477b323df636f5e3221471780da156c938ec00dda4b50639aa8d7fb9248f4")
    version("6.2.0", sha256="c98090041fa56ca4a260709876e2666f85ab7464db9454b177a189e1f52e0b1a")
    version("6.1.2", sha256="6eb7a02e5f1e5e3499206b9e74c9ccdd644abaafa2609dea0993124637617866")
    version("6.1.1", sha256="72841f112f953c16619938273370eb8727ddf6c2e00312856c9fca54db583b99")
    version("6.1.0", sha256="50386ebcb7ff24449afa2a10c76a059597464f877225c582ba3e097632a43f9c")
    version("6.0.2", sha256="e7ff4d7ac35a2dd8aad1cb40b96511a77a9c23fe4d1607902328e53728e05c28")
    version("6.0.0", sha256="99e8fa1af52d0bf382f28468e1a345af1ff3452c35914a6a7b5eeaf69fc568db")
    version("5.7.1", sha256="655e9bfef4b0b6ad3f9b89c934dc0a8377273bb0bccbda6c399ac5d5d2c1c04c")
    version("5.7.0", sha256="2c56ec5c78a36f2b847afd4632cb25dbf6ecc58661eb2ae038c2552342e6ce23")

    version("5.6.1", sha256="4de9a57c2092edf9398d671c8a2c60626eb7daf358caf710da70d9c105490221")
    version("5.6.0", sha256="30875d440df9d8481ffb24d87755eae20a0efc1114849a72619ea954f1e9206c")
    version("5.5.1", sha256="53d84ad5ba5086ed4ad67ad892c52c0e4eba8ddfa85c2dd341bf825f4d5fe4ee")
    version("5.5.0", sha256="8dbc776b56f93ddaa2ca38bf3b88299b8091de7c1b3f2e481064896cf6808e6c")
    version("5.4.3", sha256="a600eed848d47a7578c60da7e64eb92f29bbce2ec67932b251eafd4c2974cb67")
    version("5.4.0", sha256="476cd18500cc227d01f6b44c00c7adc8574eb8234b6b4daefc219650183fa090")
    version("5.3.3", sha256="aca88d90f169f35bd65ce3366b8670c7cdbe3abc0a2056eab805d0192cfd7130")
    version("5.3.0", sha256="b51dbedbe73390e0be748b92158839c82d7fa0e514fede60aa7696dc498facf0")
    version("5.2.3", sha256="978de85d3455207bb82bef2254a4624e9116b1258a8c164d7a7e21a644eff12f")
    version("5.2.1", sha256="448a7409bdc6618332a42b9503122996f26b91768140b710ba99bff8a8c03dd9")
    version("5.2.0", sha256="529e49693dd9f6459586dd0a26f14dd77dbdf8c0b45fb54830b294eba7babd27")
    version("5.1.3", sha256="479340ec34cdffbbdb1002c85a47d1fccd23e8394631a1f001ef6130be08287d")
    version("5.1.0", sha256="a5f7245059c3d28dbc037e1e6fa3f09084e29147096dd61f7ce5560291ab330f")
    version(
        "5.0.2",
        sha256="94ce313f3b37e6571778dc6865d73dafa798cbaf4de63b5307382c4a2418e99f",
        deprecated=True,
    )
    version(
        "5.0.0",
        sha256="61644365ea2b09fa7ec22f3dbdb74f2b6b1daa34b180138da9e0c856006a373e",
        deprecated=True,
    )
    version(
        "4.5.2",
        sha256="d99eddedce0a97d9970932b64b0bb4743e47d2740e8db0288dbda7bec3cefa80",
        deprecated=True,
    )
    version(
        "4.5.0",
        sha256="fbf550f243dddfef46a716e360b77c43886fed3eef67215ab9dab1c82f3851ca",
        deprecated=True,
    )
    version(
        "4.3.1",
        sha256="85fbd1645120b71635844090ce8bd9f7af0a3d1065d5fae476879f99ba0c0475",
        deprecated=True,
    )
    version(
        "4.3.0",
        sha256="2a08657a517971447fc233cb2c8ee2e117c6ab5efc31af147b28b3ef59b3847d",
        deprecated=True,
    )
    version(
        "4.2.0",
        sha256="fa0e7bcd64e97cbff7c39c9e87c84a49d2184dc977b341794770805ec3f896cc",
        deprecated=True,
    )
    version(
        "4.1.0",
        sha256="c223a5f7ccac280520abb6ea49fdd36fa9468718098a9d984be6ef839ccbc6db",
        deprecated=True,
    )
    version(
        "4.0.0",
        sha256="e84c48e80ea38698a5bd5da3940048ad3cab3696d10a53132acad07ca357f17c",
        deprecated=True,
    )
    version(
        "3.10.0",
        sha256="58866d8acdb6cc45227f2412098e37c65908b20ed3dd54901dfb515c15ad5f71",
        deprecated=True,
    )
    version(
        "3.9.0",
        sha256="d722fb61f62037894957856f2c2d17231c4622bdf75db372321ee30206dceeb6",
        deprecated=True,
    )
    version(
        "3.8.0",
        sha256="1dfad4d89d6c099e15073ed38e083bcf6cc463470dcc8a1e1b9e22060c060c72",
        deprecated=True,
    )
    version(
        "3.7.0",
        sha256="0071d14431f73ce74574e61d0786f2b7cf34b14ea898a1f54b6e1b06b2d468c0",
        deprecated=True,
    )
    version(
        "3.5.0",
        sha256="52c12eec3e3404c0749c70f156229786ee0c3e6d3c979aed9bbaea500fa1f3b8",
        deprecated=True,
    )


    variant("shared", default=True, description="Build shared or static library")
    variant("image", default=True, description="build with or without image support")
    variant("asan", default=False, description="Build with address-sanitizer enabled or disabled")

    # depends_on("c", type="build")
    # depends_on("cxx", type="build")

    depends_on("cmake@3:", type="build")
    depends_on("pkgconfig", type="build")

    # Note, technically only necessary when='@3.7: +image', but added to all
    # to work around https://github.com/spack/spack/issues/23951
    depends_on("xxd", when="+image", type="build")
    depends_on("elf", type="link")
    depends_on("numactl")
    depends_on("pkgconfig")
    depends_on("libdrm", when="@6.3:")

    for ver in [
        "3.5.0",
        "3.7.0",
        "3.8.0",
        "3.9.0",
        "3.10.0",
        "4.0.0",
        "4.1.0",
        "4.2.0",
        "4.3.0",
        "4.3.1",
        "4.5.0",
        "4.5.2",
        "5.0.0",
        "5.0.2",
        "5.1.0",
        "5.1.3",
        "5.2.0",
        "5.2.1",
        "5.2.3",
        "5.3.0",
        "5.3.3",
        "5.4.0",
        "5.4.3",
        "5.5.0",
        "5.5.1",
        "5.6.0",
        "5.6.1",
        "master",
        "5.7.0",
        "5.7.1",
        "6.0.0",
        "6.0.2",
        "6.1.0",
        "6.1.1",
        "6.1.2",
        "6.2.0",
        "6.2.1",
        "6.2.4",
    ]:
        depends_on(f"hsakmt-roct@{ver}", when=f"@{ver}")

    for ver in [
        "3.5.0",
        "3.7.0",
        "3.8.0",
        "3.9.0",
        "3.10.0",
        "4.0.0",
        "4.1.0",
        "4.2.0",
        "4.3.0",
        "4.3.1",
        "4.5.0",
        "4.5.2",
        "5.0.0",
        "5.0.2",
        "5.1.0",
        "5.1.3",
        "5.2.0",
        "5.2.1",
        "5.2.3",
        "5.3.0",
        "5.3.3",
        "5.4.0",
        "5.4.3",
        "5.5.0",
        "5.5.1",
        "5.6.0",
        "5.6.1",
        "master",
        "5.7.0",
        "5.7.1",
        "6.0.0",
        "6.0.2",
        "6.1.0",
        "6.1.1",
        "6.1.2",
        "6.2.0",
        "6.2.1",
        "6.2.4",
        "6.3.0",
        "6.3.1",
        "6.3.2",
        "6.3.3",
        "6.4.0",
        "6.4.1",
        "6.4.2",
        "6.4.3",
        "7.0.0",
        "7.0.2",
        "7.1.0",
        "7.1.1",
        "7.2.0",
    ]:
        depends_on(f"llvm-amdgpu@{ver}", when=f"@{ver}")
        depends_on(f"rocm-core@{ver}", when=f"@{ver}")

    for ver in [
        "3.5.0",
        "3.7.0",
        "3.8.0",
        "3.9.0",
        "3.10.0",
        "4.0.0",
        "4.1.0",
        "4.2.0",
        "4.3.0",
        "4.3.1",
        "4.5.0",
        "4.5.2",
        "5.0.0",
        "5.0.2",
        "5.1.0",
        "5.1.3",
        "5.2.0",
        "5.2.1",
        "5.2.3",
        "5.3.0",
        "5.3.3",
        "5.4.0",
        "5.4.3",
        "5.5.0",
        "5.5.1",
        "5.6.0",
        "5.6.1",
        "master",
    ]:
        # allow standalone rocm-device-libs (useful for aomp)
        depends_on(
            "rocm-device-libs@" + ver, when="@{0} ^llvm-amdgpu ~rocm-device-libs".format(ver)
        )

    for ver in [
        "6.3.0",
        "6.3.1",
        "6.3.2",
        "6.3.3",
        "6.4.0",
        "6.4.1",
        "6.4.2",
        "6.4.3",
        "7.0.0",
        "7.0.2",
        "7.1.0",
        "7.1.1",
        "7.2.0",
    ]:
        depends_on(f"rocprofiler-register@{ver}", when=f"@{ver}")

    patch("0001-Do-not-set-an-explicit-rpath-by-default-since-packag.patch", when="@3.5.0")
    patch("0002-Remove-explicit-RPATH-again.patch", when="@3.7.0:5.6")

    @property
    def root_cmakelists_dir(self):
        if self.spec.satisfies("@7.2:"):
            return "projects/rocr-runtime"
        elif self.spec.satisfies("@6.3:"):
            return "."
        else:
            return "src"

    @classmethod
    def determine_version(cls, lib):
        match = re.search(r"lib\S*\.so\.\d+\.\d+\.(\d)(\d\d)(\d\d)", lib)
        if match:
            ver = "{0}.{1}.{2}".format(
                int(match.group(1)), int(match.group(2)), int(match.group(3))
            )
        else:
            ver = None
        return ver

    def setup_build_ronment(self, env) -> None:
        if self.spec.satisfies("@5.7: +asan"):
            numa_inc = self.spec["numactl"].prefix.include
            numa_lib = self.spec["numactl"].prefix.lib
            env.set("CC", f"{self.spec['llvm-amdgpu'].prefix}/bin/clang")
            env.set("CXX", f"{self.spec['llvm-amdgpu'].prefix}/bin/clang++")
            env.set("ASAN_OPTIONS", "detect_leaks=0")
            env.set("CFLAGS", f"-fsanitize=address -shared-libasan -I{numa_inc} -L{numa_lib}")
            env.set("CXXFLAGS", f"-fsanitize=address -shared-libasan -I{numa_inc} -L{numa_lib}")
            env.set("LDFLAGS", "-fuse-ld=lld")

    def cmake_args(self):
        spec = self.spec

        # hsa-rocr-dev wants the directory containing the header files, but
        # libelf adds an extra path (include/libelf) compared to elfutils
        libelf_include = os.path.dirname(
            find_headers("libelf", spec["elf"].prefix.include, recursive=True)[0]
        )

        args = [
            self.define("LIBELF_INCLUDE_DIRS", libelf_include),
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("IMAGE_SUPPORT", "image"),
            self.define("CMAKE_INSTALL_LIBDIR", "lib"),
        ]

        # device libs is bundled with llvm-amdgpu (default) or standalone
        if self.spec.satisfies("^rocm-device-libs"):
            bitcode_dir = spec["rocm-device-libs"].prefix.amdgcn.bitcode
        else:
            bitcode_dir = spec["llvm-amdgpu"].prefix.amdgcn.bitcode

        args.append(self.define("BITCODE_DIR", bitcode_dir))

        if self.spec.satisfies("@5.6"):
            args.append("-DCMAKE_INSTALL_LIBDIR=lib")
        
        if self.spec.satisfies("@5.7.0:"):
            args.append(self.define_from_variant("ADDRESS_SANITIZER", "asan"))
        if self.spec.satisfies("@6.0"):
            args.append(self.define("ROCM_PATCH_VERSION", "60000"))
        if self.spec.satisfies("@6.1"):
            args.append(self.define("ROCM_PATCH_VERSION", "60100"))
        if self.spec.satisfies("@6.2"):
            args.append(self.define("ROCM_PATCH_VERSION", "60200"))
        if self.spec.satisfies("@6.3"):
            args.append(self.define("ROCM_PATCH_VERSION", "60300"))
        if self.spec.satisfies("@6.3.2:"):
            args.append(self.define("SHARED_LIBS", "ON"))
            args.append(self.define("BUILD_SHARED_LIBS", "ON"))
        return args