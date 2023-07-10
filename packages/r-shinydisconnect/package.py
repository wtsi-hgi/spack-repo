# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinydisconnect(RPackage):
    """Show a Nice Message When a 'Shiny' App Disconnects or Errors
    
    A 'Shiny' app can disconnect for a variety of reasons: an unrecoverable error occurred in
    the app, the server went down, the user lost internet connection, or any other reason
    that might cause the 'Shiny' app to lose connection to its server. With 'shinydisconnect', you can
    call disonnectMessage() anywhere in a Shiny app's UI to add a nice message when this happens. 
    Works locally (running Shiny apps within 'RStudio') and on Shiny servers (such as shinyapps.io,
    'RStudio Connect', 'Shiny Server Open Source', 'Shiny Server Pro'). See demo online at 
    <https://daattali.com/shiny/shinydisconnect-demo/>.
    """

    homepage = "https://cran.r-project.org/web/packages/shinydisconnect"
    
    cran = "shinydisconnect"

    # versions
    version("0.1.0", md5="1136ff69c9e7dfd30af2f1beb63155d1")
    

    # dependencies
    depends_on("r@3.0.0:", type=('build', 'run'))
    depends_on("r-checkmate", type=('build', 'run'))
    depends_on("r-glue", type=('build', 'run'))
    depends_on("r-htmltools", type=('build', 'run'))
    depends_on("r-shiny@1.0:", type=('build', 'run'))
    
