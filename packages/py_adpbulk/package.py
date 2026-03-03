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
#     spack install py-adpbulk
#
# You can edit this file again by typing:
#
#     spack edit py-adpbulk
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyAdpbulk(PythonPackage):
    """Performs pseudobulking of an AnnData object based on columns available in the .obs dataframe. This was originally intended to be used to pseudo-bulk single-cell RNA-seq data to higher order combinations of the data as to use existing RNA-seq differential expression tools such as edgeR and DESeq2. An example usage of this would be pseudobulking cells based on their cluster, sample of origin, or CRISPRi guide identity. This is intended to work on both individual categories (i.e. one of the examples) or combinations of categories (two of the three, etc.)"""

    homepage = "https://github.com/noamteyssier/adpbulk"
    git = "https://github.com/noamteyssier/adpbulk.git"

    license("MIT")

    version("0.1.4", commit="553e333e10279a2f519c2f4baf196aa25d639bff")

    depends_on("py-setuptools", type="build")
    depends_on("py-flit-core", type="build")
    depends_on("py-anndata", type=("build", "run"))
