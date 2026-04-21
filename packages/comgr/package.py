# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import re

from spack.package import *


class Comgr(CMakePackage):
    """This provides various Lightning Compiler related services. It currently
    contains one library, the Code Object Manager (Comgr)"""

    homepage = "https://github.com/ROCm/llvm-project"
    git = "https://github.com/ROCm/llvm-project.git"

    tags = ["rocm"]
    maintainers("srekolam", "renjithravindrankannath", "haampie", "afzpatel")
    libraries = ["libamd_comgr"]
    license("NCSA")

    def url_for_version(self, version):
        if version <= Version("6.0.2"):
            url = "https://github.com/ROCm/ROCm-CompilerSupport/archive/rocm-{0}.tar.gz"
        else:
            url = "https://github.com/ROCm/llvm-project/archive/rocm-{0}.tar.gz"
        return url.format(version)

    version("7.2.1", sha256="4d3449d758e3f79b336248b0207a394eda04ba5cdd48a4088e135ddf769127fa")
    version("7.2.0", sha256="e86138d2a63fbcbdf64668d55573b26ae944d0f0ae5a3f5bb59bf7bdb3124d3f")
    version("7.1.1", sha256="d76a16db4a56914383029e241823f7bc2a3d645f2967dd22230f11c11cfe189e")
    version("7.1.0", sha256="87f5532b8b653bd18541cdf6e59923cbd340b300d8ec5046d3e4288d9e5195c0")
    version("7.0.2", sha256="fd612fa750bebd0c3be0ea642b2cae8ff5c7e00a2280b22b9ea16ee86a11d763")
    version("7.0.0", sha256="3d479a2aa615b6bb35cd3521122fbff34188dc0cc52d8b0acda59f9f55198211")
    version("6.4.3", sha256="7a484b621d568eef000ee8c4d2d46d589e5682b950f1f410ce7215031f1f3ad7")
    version("6.4.2", sha256="9f42cb73d90bd4561686c0366f60f6e58cfd32ff24b094c69e8259fb5d177457")
    version("6.4.1", sha256="460ad28677092b9eb86ffdc49bcb4d01035e32b4f05161d85f90c9fa80239f50")
    version("6.4.0", sha256="dca1c145a23f05229d5d646241f9d1d3c5dbf1d745b338ae020eabe33beb965c")
    version("6.3.3", sha256="4df9aba24e574edf23844c0d2d9dda112811db5c2b08c9428604a21b819eb23d")
    version("6.3.2", sha256="1f52e45660ea508d3fe717a9903fe27020cee96de95a3541434838e0193a4827")
    version("6.3.1", sha256="e9c2481cccacdea72c1f8d3970956c447cec47e18dfb9712cbbba76a2820552c")
    version("6.3.0", sha256="79580508b039ca6c50dfdfd7c4f6fbcf489fe1931037ca51324818851eea0c1c")
    version("6.2.4", sha256="7af782bf5835fcd0928047dbf558f5000e7f0207ca39cf04570969343e789528")
    version("6.2.1", sha256="4840f109d8f267c28597e936c869c358de56b8ad6c3ed4881387cf531846e5a7")
    version("6.2.0", sha256="12ce17dc920ec6dac0c5484159b3eec00276e4a5b301ab1250488db3b2852200")
    version("6.1.2", sha256="300e9d6a137dcd91b18d5809a316fddb615e0e7f982dc7ef1bb56876dff6e097")
    version("6.1.1", sha256="f1a67efb49f76a9b262e9735d3f75ad21e3bd6a05338c9b15c01e6c625c4460d")
    version("6.1.0", sha256="6bd9912441de6caf6b26d1323e1c899ecd14ff2431874a2f5883d3bc5212db34")
    version("6.0.2", sha256="737b110d9402509db200ee413fb139a78369cf517453395b96bda52d0aa362b9")
    version("6.0.0", sha256="04353d27a512642a5e5339532a39d0aabe44e0964985de37b150a2550385800a")
    version("5.7.1", sha256="3b9433b4a0527167c3e9dfc37a3c54e0550744b8d4a8e1be298c8d4bcedfee7c")
    version("5.7.0", sha256="e234bcb93d602377cfaaacb59aeac5796edcd842a618162867b7e670c3a2c42c")
    version("5.6.1", sha256="0a85d84619f98be26ca7a32c71f94ed3c4e9866133789eabb451be64ce739300")
    version("5.6.0", sha256="9396a7238b547ee68146c669b10b9d5de8f1d76527c649133c75d8076a185a72")
    version("5.5.1", sha256="0fbb15fe5a95c2e141ccd360bc413e1feda283334781540a6e5095ab27fd8019")
    version("5.5.0", sha256="97dfff03226ce0902b9d5d1c8c7bebb7a15978a81b6e9c750bf2d2473890bd42")
    version("5.4.3", sha256="8af18035550977fe0aa9cca8dfacbe65fe292e971de5a0e160710bafda05a81f")
    version("5.4.0", sha256="f4b83b27ff6195679d695c3f41fa25456e9c50bae6d978f46d3541b472aef757")
    version("5.3.3", sha256="6a4ef69e672a077b5909977248445f0eedf5e124af9812993a4d444be030c78b")
    version("5.3.0", sha256="072f849d79476d87d31d62b962e368762368d540a9da02ee2675963dc4942b2c")
    version("5.2.3", sha256="36d67dbe791d08ad0a02f0f3aedd46059848a0a232c5f999670103b0410c89dc")
    version("5.2.1", sha256="ebeaea8e653fc2b9d67d3271be44690ac7876ee679baa01d47863e75362b8c85")
    version("5.2.0", sha256="5f63fa93739ee9230756ef93c53019474b6cdddea3b588492d785dae1b08c087")
    version("5.1.3", sha256="3078c10e9a852fe8357712a263ad775b15944e083f93a879935c877511066ac9")
    version("5.1.0", sha256="1cdcfe5acb768ef50fb0026d4ee7ba01e615251ad3c27bb2593cdcf8c070a894")
    version(
        "5.0.2",
        sha256="20d733f70d8edb573d8c92707f663d7d46dcaff08026cd6addbb83266679f92a",
        deprecated=True,
    )
    version(
        "5.0.0",
        sha256="da1bbc694bd930a504406eb0a0018c2e317d8b2c136fb2cab8de426870efe9a8",
        deprecated=True,
    )
    version(
        "4.5.2",
        sha256="e45f387fb6635fc1713714d09364204cd28fea97655b313c857beb1f8524e593",
        deprecated=True,
    )
    version(
        "4.5.0",
        sha256="03c5880e0922fcff31306f7da2eb9d3a3709d9b5b75b3524dcfae85f4b181678",
        deprecated=True,
    )
    version(
        "4.3.1",
        sha256="f1d99550383ed7b3a01d304eedc3d86a8e45b271aa5a80b1dd099c22fda3f745",
        deprecated=True,
    )
    version(
        "4.3.0",
        sha256="f77b505abb474078374701dfc49e651ad3eeec5349ce6edda54549943a3775ee",
        deprecated=True,
    )
    version(
        "4.2.0",
        sha256="40a1ea50d2aea0cf75c4d17cdd6a7fe44ae999bf0147d24a756ca4675ce24e36",
        deprecated=True,
    )
    version(
        "4.1.0",
        sha256="ffb625978555c63582aa46857672431793261166aa31761eff4fe5c2cab661ae",
        deprecated=True,
    )
    version(
        "4.0.0",
        sha256="f389601fb70b2d9a60d0e2798919af9ddf7b8376a2e460141507fe50073dfb31",
        deprecated=True,
    )
    version(
        "3.10.0",
        sha256="b44ee5805a6236213d758fa4b612bb859d8f774b9b4bdc3a2699bb009dd631bc",
        deprecated=True,
    )
    version(
        "3.9.0",
        sha256="6600e144d72dadb6d893a3388b42af103b9443755ce556f4e9e205ccd8ec0c83",
        deprecated=True,
    )
    version(
        "3.8.0",
        sha256="62a35480dfabaa98883d91ed0f7c490daa9bbd424af37e07e5d85a6e8030b146",
        deprecated=True,
    )
    version(
        "3.7.0",
        sha256="73e56ec3c63dade24ad351e9340e2f8e127694028c1fb7cec5035376bf098432",
        deprecated=True,
    )
    version(
        "3.5.0",
        sha256="25c963b46a82d76d55b2302e0e18aac8175362656a465549999ad13d07b689b9",
        deprecated=True,
    )

    variant("asan", default=False, description="Build with address-sanitizer enabled or disabled")

    # depends_on("c", type="build")  # generated
    # depends_on("cxx", type="build")  # generated
    # depends_on("fortran", type="build")  # generated
    
    depends_on("cmake@3.2.0:", type="build", when="@:3.8")
    depends_on("cmake@3.13.4:", type="build", when="@3.9.0:")

    depends_on("zlib-api", type="link")
    depends_on("z3", type="link")
    depends_on("ncurses", type="link")

    for ver in [
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
        "7.2.1",
    ]:
        # llvm libs are linked statically, so this *could* be a build dep
        depends_on(f"llvm-amdgpu@{ver}", when=f"@{ver}")
        depends_on(f"rocm-core@{ver}", when=f"@{ver}")
        depends_on(f"rocm-cmake@{ver}", when=f"@{ver}", type="build")

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
            depends_on("llvm-amdgpu@" + ver, when="@" + ver)
            depends_on("rocm-device-libs@" + ver, when="@{0} ^llvm-amdgpu ~rocm-device-libs".format(ver))

    for ver in ["5.5.0", "5.5.1", "5.6.0", "5.6.1"]:
        depends_on("rocm-core@" + ver, when="@" + ver)

    @property
    def root_cmakelists_dir(self):
        if self.spec.satisfies("@:6.0"):
            return join_path("lib", "comgr")
        else:
            return join_path("amd", "comgr")

    def cmake_args(self):
        args = [
            self.define("BUILD_TESTING", self.run_tests),
            self.define("CMAKE_INSTALL_LIBDIR", "lib"),
        ]
        if self.spec.satisfies("@5.7:"):
            args.append(self.define_from_variant("ADDRESS_SANITIZER", "asan"))
        return args

    def setup_build_environment(self, env) -> None:
        env.prepend_path("CMAKE_MODULE_PATH", self.spec["llvm-amdgpu"].prefix.lib.cmake.clang)
        if self.spec.satisfies("@5.7: +asan"):
            env.set("CC", f"{self.spec['llvm-amdgpu'].prefix}/bin/clang")
            env.set("CXX", f"{self.spec['llvm-amdgpu'].prefix}/bin/clang++")
            env.set("ASAN_OPTIONS", "detect_leaks=0")
            env.set("CFLAGS", "-fsanitize=address -shared-libasan")
            env.set("CXXFLAGS", "-fsanitize=address -shared-libasan")
            env.set("LDFLAGS", "-fuse-ld=lld")

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
