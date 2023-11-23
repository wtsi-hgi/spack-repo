# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.fetch_strategy import NoStageError, VCSFetchStrategy, fetcher, _needs_stage, temp_cwd
import shutil

class Fossil(AutotoolsPackage):
    """Fossil.

    Fossil is a simple, high-reliability, distributed software
    configuration management system.
    """

    homepage = "https://fossil-scm.org/"
    url = "https://github.com/drdcd/fossil-scm"

    maintainers("eschnett")

    version(
        "2.18",
        url="https://fossil-scm.org/home/tarball/84f25d7eb10c0714109d69bb2809abfa8b4b5c3d73b151a5b10df724dacd46d8/fossil-src-2.18.tar.gz",
        sha256="300c1d5cdd6224ec6e8c88ab3f38d50f80e4071b503731b75bd61274cf310733",
    )

    depends_on("openssl")

@fetcher
class FossilFetcher(VCSFetchStrategy):
    url_attr = "fossil"
    optional_attrs = [
        "tag"
    ]

    def __init__(self, **kwargs):
        super(FossilFetcher, self).__init__(**kwargs)

        self._fossil = None

    @property
    def fossil(self):
        if not self._fossil:
            self._fossil = which("fossil", required=True)
        return self._fossil

    @_needs_stage
    def fetch(self):
        if self.stage.expanded:
            tty.debug("Already fetched {0}".format(self.stage.source_path))
            return

        with temp_cwd():
            mkdir("src")
            cd("src")
            self.fossil("clone", self.url, ".fossil")
            self.fossil("open", ".fossil", self.tag)
            cd("..")
            shutil.move("src", self.stage.source_path)

    def source_id(self):
        return self.tag

    def mirror_id(self):
        return self.url + "|" + self.tag

    def archive(self, destination):
        super(FossilFetcher, self).archive(destination, exclude=".fossil")
