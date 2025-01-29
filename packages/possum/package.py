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
#     spack install possum
#
# You can edit this file again by typing:
#
#     spack edit possum
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------


import glob

from spack.package import *


class Possum(Package):
    """POSSUM (PCA Of Sparse, SUper Massive Matrices) provides R and C/C++
    functions to compute leading eigenvectors of correlation matrices from large
    sparse matrices, primarily designed for HiC contact matrices."""

    homepage = "https://github.com/moshe-olshansky/EigenVector"
    url = "https://github.com/moshe-olshansky/EigenVector/archive/refs/tags/v1.0.tar.gz"
    git = "https://github.com/moshe-olshansky/EigenVector.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list.
    license("UNKNOWN")

    version("1.0", sha256="b5459f9a6d9961ae41aa23359b8e52320d65e48c56a6563724f8fb3be15cb691")

    depends_on("r", type=("build", "run"))
    depends_on("r-strawr", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-optparse", type=("build", "run"))
    depends_on("zlib")
    depends_on("curl")

    resource(
        name="straw",
        git="https://github.com/aidenlab/straw.git",
        commit="af980f47cfc8f49a8a04bb20ebb1ce7ecdfd6012",
        destination=".",
        placement="straw",
    )

    resource(
        name="straw-v0.0.8",
        url="https://github.com/aidenlab/straw/archive/refs/tags/v0.0.8.tar.gz",
        md5="22db2baa91f2bebc25a1e50278e9b99c",
        destination=".",
        placement="straw-v0.0.8",
    )

    def patch(self):
        for cpp_file in ["getMatrix.cpp", "theEigenVector.cpp"]:
            filter_file("#include <straw.h>", '#include "straw.h"', f"C++/{cpp_file}", string=True)

    def install(self, spec, prefix):
        copy("straw/C++/straw.h", "C++/straw.h")
        copy("straw/C++/straw.cpp", "C++/straw.cpp")
        with working_dir("C++"):
            which("g++")(
                "-O2",
                "--std=c++0x",
                "-o",
                "theEigenVector.exe",
                "theEigenVector.cpp",
                "theBestEigen.c",
                "thdMul.c",
                "getMatrix.cpp",
                "straw.cpp",
                "-I.",
                "-lz",
                "-lcurl",
                "-lpthread",
            )
            which("g++")(
                "-O2",
                "--std=c++0x",
                "-o",
                "createGWEigenVector.exe",
                "createGWEigenVector.cpp",
                "theBestEigen.c",
                "thdMul.c",
                "getMatrix.cpp",
                "straw.cpp",
                "-I.",
                "-lz",
                "-lcurl",
                "-lpthread",
            )
            which("g++")(
                "-O2",
                "--std=c99",
                "-o",
                "mainEigen.exe",
                "mainEigen.c",
                "theBestEigen.c",
                "thdMul.c",
                "-lpthread",
            )

        copy("straw-v0.0.8/C++/straw.h", "C++/FlipSign/straw.h")
        copy("straw-v0.0.8/C++/straw.cpp", "C++/FlipSign/straw.cpp")
        with working_dir("C++/FlipSign"):
            which("g++")(
                "-O",
                "-o",
                "newGW_Intra_Flip.exe",
                "GWevIntra_new.cpp",
                "theBestEigen.c",
                "thdMul.c",
                "hgFlipSign.c",
                "straw.cpp",
                "-I.",
                "-lz",
                "-lcurl",
                "-lpthread",
            )
            which("g++")(
                "-O",
                "-o",
                "newSingleFlip.exe",
                "theEigenVector_flip_new.cpp",
                "theBestEigen.c",
                "thdMul.c",
                "hgFlipSign.c",
                "straw.cpp",
                "-I.",
                "-lz",
                "-lcurl",
                "-lpthread",
            )

        # Create necessary directories
        mkdirp(prefix.bin)

        # Install compiled binaries
        for exe in [
            "C++/theEigenVector.exe",
            "C++/createGWEigenVector.exe",
            "C++/mainEigen.exe",
            "C++/FlipSign/newGW_Intra_Flip.exe",
            "C++/FlipSign/newSingleFlip.exe",
        ]:
            install(exe, prefix.bin)

        # Install R scripts
        for r_file in glob.glob("*.R"):
            # add shebang
            with open(r_file, "r") as f:
                lines = f.readlines()
            lines[0] = "#!/usr/bin/env Rscript\nlibrary(optparse,quietly=TRUE)\n"
            with open(r_file, "w") as f:
                f.writelines(lines)
            filter_file(
                'source("bestEigen3.R")', f"source(\"{join_path(prefix.bin, 'bestEigen3.R')}\")", r_file, string=True
            )
            which("chmod")("+x", r_file)
            install(r_file, prefix.bin)
