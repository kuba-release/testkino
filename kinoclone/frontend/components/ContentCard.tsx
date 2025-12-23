import Image from 'next/image';
import Link from 'next/link';

interface ContentCardProps {
  content: {
    id: string;
    title: string;
    poster_url?: string;
    year?: number;
    kp_rating?: number;
  };
}

export function ContentCard({ content }: ContentCardProps) {
  return (
    <Link href={`/watch/${content.id}`} className="group cursor-pointer">
      <div className="relative aspect-[2/3] overflow-hidden rounded-lg">
        <Image
          src={content.poster_url || '/placeholder.jpg'}
          alt={content.title}
          fill
          className="object-cover transition-transform group-hover:scale-105"
        />
      </div>
      <div className="mt-2">
        <h3 className="font-semibold truncate">{content.title}</h3>
        <p className="text-sm text-gray-500">
          {content.year} • {content.kp_rating ? `★ ${content.kp_rating}` : ''}
        </p>
      </div>
    </Link>
  );
}