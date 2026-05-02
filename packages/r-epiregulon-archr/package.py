# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import inspect
import os
import tarfile

from spack.package import *


class REpiregulonArchr(RPackage):
    """Extended version of epiregulon for ArchR integration.

    Gene regulatory networks model the underlying gene regulation hierarchies
    that drive gene expression and cell states. This package extends epiregulon
    to allow for downstream analysis of single cell data prepared with the ArchR
    package. It utilizes gene expression, chromatin availability and transcription
    factor motif matches data retrieved from the ArchR project to construct
    gene regulatory networks and infer transcription factor activity in single cells."""

    homepage = "https://github.com/xiaosaiyao/epiregulon.archr/"
    url = "https://github.com/xiaosaiyao/epiregulon.archr/archive/refs/heads/master.tar.gz"

    license("MIT")

    version("0.99.5", sha256="f640df2a2c76fd928c91dbfb46b47c1b94adb9384e06e7855961c4d807e1a440", expand=False)

    def url_for_version(self, version):
        if str(version) == "0.99.5":
            return "https://github.com/xiaosaiyao/epiregulon.archr/archive/a02bd18b69944393031e77bb822a29f9afc806a0.tar.gz"
        return super().url_for_version(version)

    # Depends
    depends_on("r@4.4:", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))

    # Imports - based on the epiregulon.extra and the repository description
    depends_on("r-epiregulon", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-checkmate", type=("build", "run"))
    depends_on("r-archr", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-bluster", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-multiassayexperiment", type=("build", "run"))
    depends_on("r-rhdf5", type=("build", "run"))
    depends_on("r-scran", type=("build", "run"))
    depends_on("r-scmultiome", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))

    # Suggests
    depends_on("r-knitr", type=("build"))
    depends_on("r-rmarkdown", type=("build"))
    depends_on("r-biocstyle", type=("build"))
    depends_on("r-testthat", type=("build"))
    depends_on("r-epiregulon-extra", type=("build"))

    def install(self, spec, prefix):
        archive = self.stage.archive_file
        source_root = join_path(self.stage.path, "manual-source")
        mkdirp(source_root)

        with tarfile.open(archive, "r:gz") as tar:
            tar.extractall(source_root)

        entries = os.listdir(source_root)
        if len(entries) != 1:
            raise InstallError("Expected a single top-level epiregulon.archr source directory")

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
