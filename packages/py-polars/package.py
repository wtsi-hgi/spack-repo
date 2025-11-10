# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPolars(PythonPackage):
    """Blazingly fast DataFrame library."""

    homepage = "https://www.pola.rs/"
    pypi = "polars/polars-0.20.5.tar.gz"

    license("MIT")

    version("1.25.2", sha256="c6bd9b1b17c86e49bcf8aac44d2238b77e414d7df890afc3924812a5c989a4fe")
    version("1.20.0", sha256="e8e9e3156fae02b58e276e5f2c16a5907a79b38617a9e2d731b533d87798f451")
    version("1.19.0", sha256="b52ada5c43fcdadf64f282522198c5549ee4e46ea57d236a4d7e572643070d9d")
    version("1.18.0", sha256="5c2f119555ae8d822a5322509c6abd91601a8931115d2e4c3fff13fadf39e877")
    version("1.17.1", sha256="5a3dac3cb7cbe174d1fa898cba9afbede0c08e8728feeeab515554d762127019")
    version("1.16.0", sha256="dd99808b833872babe02434a809fd45c1cffe66a3d57123cdc5e447c7753d328")
    version("1.15.0", sha256="4f60a64ceb2e56fd0f9f403d4b6734e033876904d04cb9a29c43653c6b2b2d43")
    version("1.14.0", sha256="e34fbeca4664fba754a12d0a66b36569c4c9e5a0116108d9362067a0ca596b4d")
    version("1.13.1", sha256="a8a7bb70aca0657939552a4505eccabb07c9d59d330d5a66409fe67295082860")
    version("1.12.0", sha256="fb5c92de1a8f7d0a3f923fe48ea89eb518bdf55315ae917012350fa072bd64f4")
    version("1.11.0", sha256="4fbdd772b5f4538eb9f5ae4f3256290dba1f6c6b9d5226aed918801ed51089f4")
    version("1.10.0", sha256="855b0fffbe4fbb1c89b4f9b4b6cc724b337f946a9ba50829eb22b8a36483b3c3")
    version("1.9.0", sha256="8e1206ef876f61c1d50a81e102611ea92ee34631cb135b46ad314bfefd3cb122")
    version("1.8.2", sha256="42f69277d5be2833b0b826af5e75dcf430222d65c9633872856e176a0bed27a0")
    version("1.7.1", sha256="3323bf6b3f1cf55212ddd35f044af8a1aa02033bca17d06f3852325e0da93a80")
    version("1.6.0", sha256="d7e8d5e577883a9755bc3be92ecbf6f20bced68267bdb8bdb440120e905cc19c")
    version("1.5.0", sha256="22f767d28d76e54ff15aa38fd58c6ff9e510f22f5e20bb72e6428d70a17ba56a")
    version("1.4.1", sha256="ed8009aff8cf91f94db5a38d947185603ad5bee48a28b764cf5a52048c7c4756")
    version("1.3.0", sha256="c7812d6c72ffdc9e70aaa8f9aa6378db80b393e7ecbe7005ad84b150c17c71cb")
    version("1.2.1", sha256="a46aba51acce7ecf85151f72d25ef2a3eeb5735d55f4b7cc69ec4a596e9fbefd")
    version("1.1.0", sha256="75fe824243006ada0f2dd30c8aba0ec03595d9087b29c3ca8f106ef1a975b9cb")
    version("1.0.0", sha256="144a63d6d61dc5d675304673c4261ceccf4cfc75277431389d4afe9a5be0f70b")
    version("0.20.31", sha256="00f62dec6bf43a4e2a5db58b99bf0e79699fe761c80ae665868eaea5168f3bbb")

    # pyproject.toml
    depends_on("py-maturin@1.3.2:", type="build")

    # README.md
    depends_on("rust@1.85:", when="@1.25.2:", type="build")
    depends_on("rust@1.81:", when="@1:", type="build")
    depends_on("rust@1.71:", type="build")
    depends_on("cmake", type="build")

    def patch(self):
        # Keep upstream's Cargo.lock to preserve pinned crate versions
        # for this release. Removing it can cause Cargo to resolve to
        # newer crates that may require a newer Rust toolchain.
        if self.spec.satisfies("@1.25.2:"):
            filter_file(
                """#![cfg_attr(feature = "nightly", feature(select_unpredictable))] """,
                "",
                "crates/polars-utils/src/lib.rs",
                string=True,
            )
            with open("crates/polars-utils/src/select.rs", "r") as f:
                content = f.read()
            # only keep the final 4 lines
            content = content.split("\n")[-4:]
            with open("crates/polars-utils/src/select.rs", "w") as f:
                f.write("\n".join(content))
            

        filter_file(
            'default = ["all", "nightly"]',
            'default = ["all"]',
            "py-polars/Cargo.toml",
            string=True,
        )

    def setup_build_environment(self, env):
        env.set("CARGO_NET_GIT_FETCH_WITH_CLI", "true")
        # env.set("MATURIN_PEP517_ARGS", "--no-default-features --features lazy")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import polars")
