# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import inspect
import os
import tarfile

from spack.package import *


class RArchr(RPackage):
    """Analysis of Regulatory Chromatin in R."""

    homepage = "https://www.archrproject.com"
    url = "https://github.com/GreenleafLab/ArchR/archive/refs/tags/v1.0.2.tar.gz"
    git = "https://github.com/GreenleafLab/ArchR.git"

    maintainers("dorton21")

    version("1.0.3", sha256="9e3c5f07b599ff806c6f2a74ec619b0847e69cb3e96dc29fa1304f2a381620e4", expand=False)

    depends_on("r@4.0.0:", type=("build", "run"))

    with default_args(type=("build", "run")):
        depends_on("r-biocmanager")
        depends_on("r-devtools")
        depends_on("r-genomicranges")
        depends_on("r-summarizedexperiment")
        depends_on("r-iranges")
        depends_on("r-matrix")
        depends_on("r-rcpp")
        depends_on("r-rhdf5")
        depends_on("r-s4vectors")
        depends_on("r-data-table")
        depends_on("r-ggplot2")
        depends_on("r-plyr")
        depends_on("r-stringr")
        depends_on("r-magrittr")
        depends_on("r-pbapply")
        depends_on("r-nabor")
        depends_on("r-mass")
        depends_on("r-motifmatchr")
        depends_on("r-chromvar")
        depends_on("r-complexheatmap")
        depends_on("r-rsamtools")
        depends_on("r-biostrings")
        depends_on("r-bsgenome")
        depends_on("r-genomeinfodb")
        depends_on("r-rtracklayer")
        depends_on("r-uwot")
        depends_on("r-rann")
        depends_on("r-seurat")
        depends_on("r-biocgenerics")
        depends_on("r-monocle3")
        depends_on("r-slingshot")
        depends_on("r-presto")
        depends_on("r-harmony")
        depends_on("r-chromvarmotifs")
        depends_on("r-shiny")
        depends_on("r-shinythemes")
        depends_on("r-cairo")
        depends_on("r-ggrastr")
        depends_on("r-rhandsontable")

    def install(self, spec, prefix):
        archive = self.stage.archive_file
        source_root = join_path(self.stage.path, "manual-source")
        mkdirp(source_root)

        with tarfile.open(archive, "r:gz") as tar:
            tar.extractall(source_root)

        entries = os.listdir(source_root)
        if len(entries) != 1:
            raise InstallError("Expected a single top-level ArchR source directory")

        source_path = join_path(source_root, entries[0])
        compact_r_libs = join_path(self.stage.path, "compact-r-libs")
        mkdirp(compact_r_libs)
        for dep in spec.traverse(root=False):
            if not dep.name.startswith("r-"):
                continue
            dep_lib_root = join_path(dep.prefix, "rlib", "R", "library")
            if not os.path.isdir(dep_lib_root):
                continue
            for entry in os.listdir(dep_lib_root):
                src = join_path(dep_lib_root, entry)
                dst = join_path(compact_r_libs, entry)
                if not os.path.exists(dst):
                    os.symlink(src, dst)

        args = ["--vanilla", "CMD", "INSTALL", "--library={0}".format(self.module.r_lib_dir), source_path]
        original_r_libs = os.environ.get("R_LIBS")
        os.environ["R_LIBS"] = "{0}:{1}".format(compact_r_libs, self.module.r_lib_dir)
        try:
            inspect.getmodule(self).R(*args)
        finally:
            if original_r_libs is None:
                os.environ.pop("R_LIBS", None)
            else:
                os.environ["R_LIBS"] = original_r_libs
