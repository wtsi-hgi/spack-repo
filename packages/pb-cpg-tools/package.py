# Copyright 2013-2023 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT file
# for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PbCpgTools(Package):
    """PacBio CLI that converts aligned HiFi reads with CpG modification tags
    into bed and bigWig methylation tracks using a TensorFlow Lite scoring
    model."""

    homepage = "https://github.com/PacificBiosciences/pb-CpG-tools"
    url = "https://github.com/PacificBiosciences/pb-CpG-tools/archive/refs/tags/v3.0.0.tar.gz"

    license("LicenseRef-PacBio-Software-License")

    version("3.0.0", sha256="bf208327f3ba69c60cdefc931f934ffdcb8b57d1bf1bb0319da89f59fb265b8a")

    variant("tflite", default=True, description="Enable TensorFlow Lite powered pileup model")

    def patch(self):
        before = """    let gitcl = GitclBuilder::default()
        .describe(true, true, None)
        .build()
        .unwrap();
    Emitter::default()
        .fail_on_error()
        .add_instructions(&gitcl)
        .unwrap()
        .emit()
        .unwrap();
"""
        after = """    if let Ok(gitcl) = GitclBuilder::default()
        .describe(true, true, None)
        .build()
    {
        let mut emitter = Emitter::default();
        match emitter.add_instructions(&gitcl) {
            Ok(emitter) => {
                if let Err(err) = emitter.emit() {
                    println!("cargo:warning=vergen git metadata disabled: {err}");
                }
            }
            Err(err) => {
                println!("cargo:warning=vergen git metadata disabled: {err}");
            }
        }
    }

"""
        with open("build.rs", "r", encoding="utf-8") as fh:
            contents = fh.read()
        if before not in contents:
            raise RuntimeError("expected vergen block not found in build.rs")
        contents = contents.replace(before, after, 1)
        with open("build.rs", "w", encoding="utf-8") as fh:
            fh.write(contents)

    depends_on("rust@1.74:+dev", type="build")
    depends_on("cmake@3.16:", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("zlib-api", type=("build", "link"))
    depends_on("llvm+clang", when="+tflite", type=("build", "link"))

    def setup_build_environment(self, env):
        if "+tflite" in self.spec:
            env.set("LIBCLANG_PATH", join_path(self.spec["llvm"].prefix, "lib"))

    def install(self, spec, prefix):
        cargo = which("cargo")
        args = ["install", "--locked", "--root", prefix, "--path", "."]
        if "+tflite" in spec:
            args += ["--features", "tflite"]
        cargo(*args)

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            exe = Executable(join_path(self.prefix.bin, "aligned_bam_to_cpg_scores"))
            exe("--help")
