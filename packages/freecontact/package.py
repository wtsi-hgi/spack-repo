# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Freecontact(AutotoolsPackage):
    """ FreeContact is a protein residue contact predictor optimized for speed. Its input is a multiple sequence alignment. FreeContact can function as an accelerated drop-in for the published contact predictors EVfold-mfDCA of DS. Marks (2011) and PSICOV of D. Jones (2011). """

    homepage = "http://rostlab.org/owiki/index.php/FreeContact"
    url = "http://deb.debian.org/debian/pool/main/f/freecontact/freecontact_1.0.21.orig.tar.xz"

    version("1.0.21", sha256="513c503ace70abc3cbc12d1aff616ffd9b6564a73a584efd7435b804479bd2a8")

    depends_on("boost+program_options")
    depends_on("openblas")

    def patch(self):
        filter_file("#endif // __SSE2__", "#endif // __SSE2__\n#define throw(...)", "lib/freecontact.h", string=True)

    def configure_args(self):
        return [
            "--with-boost=" + self.spec["boost"].prefix.include.boost,
            "--with-boost-libdir=" + self.spec["boost"].prefix.lib,
        ]
