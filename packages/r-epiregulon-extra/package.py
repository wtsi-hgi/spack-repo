# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install r-epiregulon-extra
#
# You can edit this file again by typing:
#
#     spack edit r-epiregulon-extra
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

import inspect
import os
import tarfile

from spack.package import *


class REpiregulonExtra(RPackage):
    """Companion package to epiregulon with additional plotting, differential and graph functions.

    Gene regulatory networks model the underlying gene regulation hierarchies
    that drive gene expression and observed phenotypes. Epiregulon infers TF
    activity in single cells by constructing a gene regulatory network (regulons).
    This is achieved through integration of scATAC-seq and scRNA-seq data and
    incorporation of public bulk TF ChIP-seq data. Links between regulatory
    elements and their target genes are established by computing correlations
    between chromatin accessibility and gene expressions."""

    homepage = "https://github.com/xiaosaiyao/epiregulon.extra/"
    urls = [
        "https://mghp.osn.xsede.org/bir190004-bucket01/archive.bioconductor.org/packages/3.21/bioc/src/contrib/epiregulon.extra_1.4.0.tar.gz",
        "https://mghp.osn.xsede.org/bir190004-bucket01/archive.bioconductor.org/packages/3.20/bioc/src/contrib/Archive/epiregulon.extra/epiregulon.extra_1.2.1.tar.gz",
    ]
    bioc = "epiregulon.extra"

    license("MIT")

    version("1.4.0", sha256="6cacb9854584df916c98cf7ba459833228748126ec70d4cbd276c23db90aac22", expand=False)
    version("1.2.2", commit="aa85b232399d3cb21b06887f999adc52ad6d1e87")

    # Depends
    depends_on("r@4.4:", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))

    # Imports
    depends_on("r-scran", type=("build", "run"))
    depends_on("r-complexheatmap", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-checkmate", type=("build", "run"))
    depends_on("r-circlize", type=("build", "run"))
    depends_on("r-clusterprofiler", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-ggraph", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-lifecycle", type=("build", "run"))
    depends_on("r-patchwork", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-scater", type=("build", "run"))

    # Suggests
    depends_on("r-epiregulon", type=("build"))
    depends_on("r-knitr", type=("build"))
    depends_on("r-rmarkdown", type=("build"))
    depends_on("r-biocstyle", type=("build"))
    depends_on("r-testthat@3.0.0:", type=("build"))
    depends_on("r-enrichmentbrowser", type=("build"))
    depends_on("r-msigdbr", type=("build"))
    depends_on("r-dorothea", type=("build"))
    depends_on("r-scmultiome", type=("build"))
    depends_on("r-s4vectors", type=("build"))
    depends_on("r-scuttle", type=("build"))
    depends_on("r-vdiffr", type=("build"))
    depends_on("r-ggrastr", type=("build"))
    depends_on("r-ggrepel", type=("build"))

    def install(self, spec, prefix):
        archive = self.stage.archive_file
        source_root = join_path(self.stage.path, "manual-source")
        mkdirp(source_root)

        with tarfile.open(archive, "r:gz") as tar:
            tar.extractall(source_root)

        entries = os.listdir(source_root)
        if len(entries) != 1:
            raise InstallError("Expected a single top-level epiregulon.extra source directory")

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
