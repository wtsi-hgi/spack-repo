# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class Rust(Package):
    """The Rust programming language toolchain."""

    homepage = "https://www.rust-lang.org"
    url = "https://static.rust-lang.org/dist/rustc-1.42.0-src.tar.gz"
    git = "https://github.com/rust-lang/rustup"
    
    version("1.96.0", tag="main")
    version("1.92.0", tag="main")
    version("1.88.0", tag="main")
    version("1.86.0", tag="main")
    version("1.85.0", tag="main")
    version("1.83.0", tag="main")
    version("1.81.0", tag="main")
    version("1.80.0", tag="main")
    version("1.79.0", tag="main")
    version("1.78.0", tag="main")
    version("1.76.0", tag="main")
    version("1.75.0", tag="main")
    version("1.74.0", tag="main")
    version("1.73.0", tag="main")
    version("1.70.0", tag="main")
    version("1.65.0", tag="main")
    version("1.60.0", tag="main")

    depends_on("curl", type="build")

    def install(self, spec, prefix):
        os.environ["CARGO_HOME"] = join_path(prefix, "cargo")
        os.environ["RUSTUP_HOME"] = join_path(prefix, "rustup")
        
        os.environ["RUSTUP_INIT_SKIP_PATH_CHECK"] = "yes"

        Executable(self.stage.source_path + "/rustup-init.sh")(
            "-y",
            "--no-modify-path",
            "--default-toolchain",
            str(spec.version)
        )

        os.symlink(join_path(prefix, "cargo", "bin"), prefix.bin)

    def setup_dependent_build_environment(self, env, dependent_spec):
        env.set("CARGO_HOME", join_path(self.prefix, "cargo"))
        env.set("RUSTUP_HOME", join_path(self.prefix, "rustup"))
        env.prepend_path("PATH", self.prefix.bin)

    def setup_run_environment(self, env):
        env.set("CARGO_HOME", join_path(self.prefix, "cargo"))
        env.set("RUSTUP_HOME", join_path(self.prefix, "rustup"))
        env.prepend_path("PATH", self.prefix.bin)
