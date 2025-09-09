# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import json
import re
from spack.package import *
import urllib.request
import urllib.error

class RMaveqc(RPackage):
    """A R package of quality control on SGE data."""

    homepage = "https://gitlab.internal.sanger.ac.uk/sci/MAVEQC"
    git = "https://gitlab.internal.sanger.ac.uk/sci/MAVEQC"
    url = "https://gitlab.internal.sanger.ac.uk/sci/MAVEQC/-/archive/0.2.9.229/MAVEQC-0.2.9.229.tar.gz"


    version("0.2.9.229", sha256="821eaa65b163c2d2a83231d57c679e1c5de9493e7a084c6511298d5ea2649655")
    version("0.2.8.229", sha256="f596ee6726ce192685f8c7ca8db1a80024a1d93587ee6bd474e4ad861a5597df")
    version("0.2.7", sha256="d3af08fe6865c4a62189c2c67e96b1eae955a255dcf24b15e6ed2650d34905fd")
    version("0.2.6", sha256="3bea0ce26aa97610318e1ada3bf12352439aff6f31306b661d19215354d5f952")
    version("0.2.5", sha256="a5d5edac113c82cf4626020958cc296aeddbdf198b44573af8c4cf3b33d171f1")
    version("0.2.4", sha256="e8a2781ec97f16fedf5ca49815fa49e3c5aed66fbcdb1784a5e40847dba052b7")
    version("0.2.3", sha256="2f0cc1d2a64340c5f557c95d76fe417bee0b0b82a8eb10bc7e574314e2b26c5e")
    version("0.2.2", sha256="13bc355a46b8daf18e49deb4fc84805c4a770db59b208435fbe3a7d7b0f1112d")
    version("0.2.1", sha256="1953db255b93708be8636e3423a97a7d22aeb24ac642e0e268ab0211af0a83d9")
    version("0.2.0", sha256="f4a1285f3f4feafeb56773449b5afa7c7c7b113b29fce621ba014cff42eefa1e")
    version("0.1.1", sha256="dd69f43b827b83b69ea208721f2e3dc278d305108d62c1a36b7e333e5841eed2")
    version("0.1.0", sha256="18e76c8353f706dc887a687e197c5923c2192bae532ed8cd7ea02f3e85e7fc23")

    depends_on("pandoc", type=("build", "run"))

    depends_on("r+X@4.3:", type=("build", "run"))
    depends_on("r+X@4.3.2:", type=("build", "run"), when="@0.2.6:")
    depends_on("r-optparse@1.7.3", type=("build", "run"))
    depends_on("r-configr", type=("build", "run"))
    depends_on("r-vroom@1.6.3:", type=("build", "run"))
    depends_on("r-data-table@:1.14.10", type=("build", "run"))
    depends_on("r-ckmeans-1d-dp", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-plotly@4.10.2:", type=("build", "run"))
    depends_on("r-ggcorrplot", type=("build", "run"))
    depends_on("r-corrplot", type=("build", "run"))
    depends_on("r-deseq2@1.38.3:", type=("build", "run"))
    depends_on("r-degreport", type=("build", "run"))
    depends_on("r-apeglm", type=("build", "run"))
    depends_on("r-see", type=("build", "run"))
    depends_on("r-ggbeeswarm@0.7.2:", type=("build", "run"))
    depends_on("r-reactable", type=("build", "run"))
    depends_on("r-htmltools@0.5.5:", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-gtools", type=("build", "run"))
    depends_on("r-sparkline", type=("build", "run"))
    depends_on("r-dendextend", type=("build", "run"))

    def fetch_remote_versions(self, *args, **kwargs):
        """Fetch available versions from GitLab API"""

        
        # GitLab API endpoint for tags
        api_url = "https://gitlab.internal.sanger.ac.uk/api/v4/projects/sci%2FMAVEQC/repository/tags"
        
        try:
            # Fetch tags from GitLab API
            with urllib.request.urlopen(api_url) as response:
                tags_data = json.loads(response.read().decode('utf-8'))
            
            # Extract version names from tags
            versions = {}
            for tag in tags_data:
                version_name = tag['name']
                # Skip non-version tags (like 'main', 'develop', etc.)
                if re.match(r'^\d+\.\d+\.\d+(\.\d+)?$', version_name):
                    versions[Version(version_name)] = self.url_for_version(version_name)
            
            return versions
            
        except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError) as e:
            # If API call fails, fall back to existing versions
            # This ensures the package still works even if the API is unavailable
            return {}
