import { Helmet } from 'react-helmet-async';

interface SEOProps {
    title?: string;
    description?: string;
    canonical?: string;
    noindex?: boolean;
}

export const SEO = ({
    title = "Gist - Everything is Simpler",
    description = "Gist - The ultimate text manipulation and jargon simplification tool. Translate complex corporate and legal speak into everyday language instantly.",
    canonical = "https://gist.ai/",
    noindex = false
}: SEOProps) => {
    const fullTitle = title.includes('Gist') ? title : `${title} | Gist`;

    return (
        <Helmet>
            <title>{fullTitle}</title>
            <meta name="description" content={description} />
            <link rel="canonical" href={canonical} />

            {/* Open Graph / Facebook */}
            <meta property="og:type" content="website" />
            <meta property="og:url" content={canonical} />
            <meta property="og:title" content={fullTitle} />
            <meta property="og:description" content={description} />
            <meta property="og:image" content="https://gist.ai/og-image.jpg" /> {/* Placeholder, user to update */}

            {/* Twitter */}
            <meta name="twitter:card" content="summary_large_image" />
            <meta name="twitter:url" content={canonical} />
            <meta name="twitter:title" content={fullTitle} />
            <meta name="twitter:description" content={description} />
            <meta name="twitter:image" content="https://gist.ai/og-image.jpg" />

            {noindex && <meta name="robots" content="noindex, nofollow" />}
            <html lang="en" />
        </Helmet>
    );
};
