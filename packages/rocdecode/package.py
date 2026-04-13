# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class Rocdecode(CMakePackage):
    """rocDecode is a high performance video decode SDK for AMD hardware"""

    homepage = "https://github.com/ROCm/rocDecode"
    git = "https://github.com/ROCm/rocDecode.git"
    url = "https://github.com/ROCm/rocDecode/archive/refs/tags/rocm-7.2.0.tar.gz"

    tags = ["rocm"]

    maintainers("afzpatel", "srekolam", "renjithravindrankannath")

    license("MIT")
    version("7.2.0", sha256="70c3828364a289098123111aa27d37bab7238065b6ee8ceae35810ad4842bf0a")
    version("7.1.1", sha256="76e7a27eb49b262ed68c2c8f13a20aba8700113087bc58068c396979e6051596")
    version("7.1.0", sha256="ccd8d7fe8010214a00d75ac0299747ad9ebf25849f2575cb096b814ec071d952")
    version("7.0.2", sha256="4d8c49236135105f252fe6ccd8652a440b4646129cad8595eead49cc7d34aa96")
    version("7.0.1", sha256="9c54b0f3846d64b5f48d33e3fe4decf3f1d471682d4540152456e46af56c2802")
    version("7.0.0", sha256="f0c1dd260bf091c44d15718008630d0b882b8f444f4740c9d8edcbbed1e759fe")
    version("6.4.4", sha256="5988ba29af103410cdff9d3d3701ffdcf73fbc9b8b90d2cd1a70d1e5ae838983")
    version("6.4.3", sha256="dd485e1cf24eb6f7315c32afcd2eb639a64dfb100a747bdbef3aa3235c4e3fa9")
    version("6.4.2", sha256="43c3bc2fe71c150bd6e646c95f834002df80d0bc6489082731c0be68fb785eac")
    version("6.4.1", sha256="35e364cec1405c76cfbb91215e1a327efea1e60340d8c8df12c0e5b2f0e1321e")
    version("6.4.0", sha256="d82c17687cc8ccac67fe2d401edd25c9825b38777b7a7b4100f84658838a1e50")
    version("6.3.3", sha256="e72f53674527b7a6c3cba3b7555fee32117f0875107fd9e632a2ec1d5ce03489")
    version("6.3.2", sha256="39ff3c21c81a73910dcfe6a147edaddecc21575a3077f0f99971c8d2f6d0e7d5")
    version("6.3.1", sha256="94da1a61167abaf3f983ae5d62bffb22bb8ba3eb1c9d9fc7c68ed9a066aa4e52")
    version("6.3.0", sha256="931f49ff86fa34929b03cec8e7becde78d0c49c1c3a23a13203fecd2b392b242")
    version("6.2.4", sha256="37aaa1299cfc517ddaf60b0e8a5cf06d672f59e8acc0da3862b40b810d4931cb")
    version("6.2.2", sha256="ecd4717be3d4154c2284cb4eee1d3099c76ed64780c2e50f4b49f21fe8a0c697")
    version("6.2.1", sha256="d4a636415d61fef94f97197cb9ebbff59e3a18dc4850612ee142e3e14a35e6d4")
    version("6.2.0", sha256="fe0d7c19a4e65b93405566511880b94f25ef68c830d0088f9458da9baea1d4f9")
    version("6.1.5", sha256="832cc548dc9b830a9afe3173b02ee720ddd0d160b0a149cbea9f69cfdee6dbd7")
    version("6.1.2", sha256="67a13aeaa495e06683124de5908e61cf2be3beff79b13d858897344aa809775e")
    version("6.1.1", sha256="5914c91e433ec7e8511b8a9017d165a0589c1aff9f5527b413d0b3a32a3cc318")
    version("6.1.0", sha256="8316dbde87f1fea782af6216c8d013e866542329a673fb24a668335c6169ef8f")

    amdgpu_targets = ROCmPackage.amdgpu_targets

    variant(
        "amdgpu_target",
        description="AMD GPU architecture",
        values=auto_or_any_combination_of(*amdgpu_targets),
        sticky=True,
    )

    depends_on("cmake@3.16:", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("libdrm", type=("build", "link", "run"))
    depends_on("libva", type=("build", "link", "run"))

    depends_on("hip@5.6.1:", when="@6.1:")
    depends_on("llvm-amdgpu@5.6.1:", when="@6.1:")

    def patch(self):
        filter_file(
            r"${ROCM_PATH}/llvm/bin/clang++",
            "{0}/bin/clang++".format(self.spec["llvm-amdgpu"].prefix),
            "CMakeLists.txt",
            string=True,
        )
        filter_file(
            r"${ROCM_PATH}/lib/llvm/bin/clang++",
            "{0}/bin/clang++".format(self.spec["llvm-amdgpu"].prefix),
            "CMakeLists.txt",
            string=True,
        )

    def cmake_args(self):
        args = []
        if "auto" not in self.spec.variants["amdgpu_target"]:
            args.append(self.define_from_variant("AMDGPU_TARGETS", "amdgpu_target"))
        if self.spec.satisfies("@6.3.0:"):
            args.append(self.define("LIBVA_INCLUDE_DIR", self.spec["libva"].prefix.include))
        return args

    @run_after("install")
    def install_test(self):
        lib_dirs = []
        for attr in ("lib", "lib64"):
            path = getattr(self.prefix, attr, None)
            if path:
                lib_dirs.append(path)
        target = None
        for lib_dir in lib_dirs:
            candidate = join_path(lib_dir, "librocdecode.so")
            if os.path.exists(candidate):
                target = candidate
                break
        if target is None:
            target = join_path(self.prefix.lib, "librocdecode.so")
        self.run_test(
            "test",
            options=["-f", target],
            purpose="check rocDecode shared library is installed",
        )
