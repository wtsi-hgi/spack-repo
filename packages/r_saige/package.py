# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class RSaige(RPackage):
    """SAIGE is an R package developed with Rcpp for genome-wide association tests in large-scale data sets and biobanks. The method

    accounts for sample relatedness based on the generalized mixed models
    allows for model fitting with either full or sparse genetic relationship matrix (GRM)
    works for quantitative and binary traits
    handles case-control imbalance of binary traits
    computationally efficient for large data sets
    performs single-variant association tests
    provides effect size estimation through Firth’s Bias-Reduced Logistic Regression
    performs conditional association analysis"""

    homepage = "https://saigegit.github.io/SAIGE-doc/"
    url = "https://github.com/saigegit/SAIGE/archive/refs/tags/v1.3.3.tar.gz"
    git = "https://github.com/saigegit/SAIGE"

    # Latest development snapshot designated as version 1.5
    version("1.5", commit="0bbda8d4aceaf98f909f295de1bbd04b565c9dea")

    version("1.3.3", sha256="7d67ae1cd140dc883e3429d9538b6cb42feef04602f7c53e429e22c790e67440")
    version("1.3.1", commit="92b6c6cd7f552d340cfc4b3b395574fbc598ee2e")
    version("1.0.9", sha256="eb5030877faf4a50d39ae28d6cd9b4aa8059cba42e1c91a4b20c32581a9f75f9")
    version("1.0.4", sha256="4b9dd64648b2c807aeda448c8b96091164ce019800efc8ebf5dc87979e590d08")
    version("1.0.3", sha256="79bcdc2abc68d8f112086a3d872102f5714bb0baaf59e876e9f08b1ad3a45e9f")
    version("1.0.2", sha256="57f4c89f78b0be5a8a00be1a507fb6cedd09fc747e683acb4a6295b6901034cb")
    version("1.0.1", sha256="7bf0bc07929eab047e042604283dc696d80e1a11e69faa8e6b0f16d85bcfaac9")
    version("1.0.0", sha256="e5870bb08ce96bf01d97fbee4887242e471f5622d0d58e7e8f0e8916d32b91fc")

    # Additional resources required for 1.5 and above
    resource(
        name="plink-ng",
        when="@1.5:",
        url="https://github.com/chrchang/plink-ng/archive/refs/tags/v2.0.0-a.6.16.tar.gz",
        sha256="eb2a15ae9cd9106d233850912255bfec4e5d5c32a2fb24e34db265ccf9fb9f52",
        placement="plink-ng",
    )

    resource(
        name="savvy",
        when="@1.5:",
        url="https://github.com/statgen/savvy/archive/5d0cd9da476223e2bbe1c85d02601fbe148aadbb.tar.gz",
        sha256="fed36eb4c3b2f3274b23c6c13db633cf37d3f2044de5187658f7920c2c7266b8",
        placement="savvy",
    )

    resource(
        name="shrinkwrap",
        when="@1.5:",
        url="https://github.com/jonathonl/shrinkwrap/archive/refs/tags/v1.2.0.tar.gz",
        sha256="aa15583079c3dfccb118cf36fae9bc6353920b99d0204a9e349dad027b531286",
        placement="shrinkwrap",
    )

    depends_on("r@3.6.1:", type=("build", "run"))
    # Build-time tools only
    depends_on("cmake", type="build")
    depends_on("cget", type="build")
    depends_on("blas")
    depends_on("lapack")
    depends_on("r-rcpp@1.0.7:", type=("build", "run"))
    depends_on("r-rcpparmadillo", type=("build", "run"))
    depends_on("r-rcppparallel", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-spatest@3.1.2", type=("build", "run"))
    depends_on("r-rcppeigen", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-bh", type=("build", "run"))
    depends_on("r-optparse", type=("build", "run"))
    depends_on("r-skat", type=("build", "run"))
    depends_on("r-metaskat", type=("build", "run"))
    depends_on("r-rsqlite", type=("build", "run"))
    depends_on("r-qlcmatrix", type=("build", "run"))
    depends_on("r-rhpcblasctl", type=("build", "run"))
    depends_on("r-roxygen2", type=("build", "run"))
    depends_on("r-rversions", type=("build", "run"))
    depends_on("r-devtools", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-dbplyr", type=("build", "run"))
    depends_on("r-lintools", type=("build", "run"), when="@1.5:")
    depends_on("r-survival", type=("build", "run"), when="@1.5:")
    depends_on("zstd", when="@1.5:")
    depends_on("libdeflate", when="@1.5:")
    depends_on("zlib", when="@1.5:")
    depends_on("superlu", when="@1.5:")

    def patch(self):
        # Ensure LAPACK/BLAS linkage uses Spack-provided libs with full paths
        lapack_flags = self.spec["lapack"].libs.ld_flags
        blas_flags = self.spec["blas"].libs.ld_flags
        filter_file(
            "-llapack",
            f"{lapack_flags} {blas_flags}",
            "src/Makevars",
            string=True,
        )

        # For 1.5+, replace pixi include path with savvy/zstd/libdeflate includes
        if self.spec.satisfies("@1.5:"):
            savvy_inc = join_path(self.stage.source_path, "savvy", "include")
            shrink_inc = join_path(self.stage.source_path, "shrinkwrap", "include")
            zstd_inc = self.spec["zstd"].prefix.include
            ldef_inc = self.spec["libdeflate"].prefix.include
            filter_file(
                r"-I\.\./\.pixi/envs/default/include",
                f"-I{savvy_inc} -I{shrink_inc} -I{zstd_inc} -I{ldef_inc}",
                "src/Makevars",
                string=True,
            )

    @run_before("install")
    def build_plink2_includes(self):
        # For 1.5+, build a shared library from plink-ng headers (mimic Dockerfile)
        if not self.spec.satisfies("@1.5:"):
            return

        from glob import glob
        cxx = which(self.compiler.cxx)
        # Construct include and library flags
        savvy_inc = str(join_path(self.stage.source_path, "savvy", "include"))
        shrink_inc = str(join_path(self.stage.source_path, "shrinkwrap", "include"))
        # plink-ng resource extracts to 'plink-ng/2.0', not nested with version dir
        p2_inc = str(join_path(self.stage.source_path, "plink-ng", "2.0", "include"))
        zstd = self.spec["zstd"].prefix
        ldef = self.spec["libdeflate"].prefix
        zlib = self.spec["zlib"].prefix

        with working_dir(self.stage.source_path):
            # Build a static archive from plink-ng sources to avoid runtime deps
            cc_files = glob(join_path(p2_inc, "*.cc"))
            obj_files = []
            for src in cc_files:
                obj = src.replace(".cc", ".o")
                cxx(
                    "-std=c++14",
                    "-fPIC",
                    "-O3",
                    "-I" + str(savvy_inc),
                    "-I" + str(p2_inc),
                    "-I" + str(shrink_inc),
                    "-I" + str(zstd.include),
                    "-I" + str(ldef.include),
                    "-I" + str(zlib.include),
                    "-c",
                    src,
                    "-o",
                    obj,
                )
                obj_files.append(obj)

            ar = which("ar")
            if obj_files:
                ar("rcs", "plink2_includes.a", *obj_files)

            # Ensure SAIGE compilation can find savvy/zstd/libdeflate headers by augmenting PKG_CPPFLAGS
            mkv = join_path(self.stage.source_path, "src", "Makevars")
            with open(mkv, "a") as fh:
                fh.write("\n# Injected by Spack: add system includes for SAIGE 1.5\n")
                fh.write(f"PKG_CPPFLAGS += -I{savvy_inc} -I{shrink_inc} -I{str(zstd.include)} -I{str(ldef.include)}\n")
                fh.write(f"PKG_LIBS += -L{str(zstd.lib)} -L{str(ldef.lib)} -lzstd -ldeflate -lz -lpthread -lm\n")
            # Replace plink2 link flags to link archive directly
            filter_file(
                r"PKG_LIBS \+= -L\.\. -l:plink2_includes\.a",
                "PKG_LIBS += ../plink2_includes.a",
                mkv,
                string=True,
            )
